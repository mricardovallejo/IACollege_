# import libraries
# https://learnopencv.com/deep-learning-with-opencvs-dnn-module-a-definitive-guide/
# Image classification for object identification
# DenseNet121 model

import cv2 #pip #install opencv-python
from matplotlib import pyplot as plt  #pip install matplotlib
import numpy as np #pip install numpy
from skimage.exposure import rescale_intensity
import argparse


# LOAD IMAGE

# load the image from disk
#image = cv2.imread('input/image_1.jpg')
image = cv2.imread('input/image_1.jpg')

# PREPROCRESS IMAGE - create blob from image
blob = cv2.dnn.blobFromImage(image=image, scalefactor=0.01, size=(224, 224), mean=(104, 117, 123))

# read the ImageNet class names
with open('input/classification_classes_ILSVRC2012.txt', 'r') as f:
    image_net_names = f.read().split('\n')

# final class names (just the first word of the many ImageNet names for one image)
class_names = [name.split(',')[0] for name in image_net_names]

# Load the Pre-Trained DenseNet121 Model from Disk
# load the neural network model
model = cv2.dnn.readNet(model='input/DenseNet_121.caffemodel', config='input/DenseNet_121.prototxt', framework='Caffe')

## PRopagate Input in Model

# set the input blob for the neural network
model.setInput(blob)

# forward pass image blog through the model
outputs = model.forward()

final_outputs = outputs[0]
# make all the outputs 1D
final_outputs = final_outputs.reshape(1000, 1)

# get the class label
label_id = np.argmax(final_outputs)
# convert the output scores to softmax probabilities
probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))
# get the final highest probability
final_prob = np.max(probs) * 100.

# map the max confidence to the class label names
out_name = class_names[label_id]
out_text = f"{out_name}, {final_prob:.3f}"

# put the class name text on top of the image
cv2.putText(image, out_text, (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.imwrite('result_image.jpg', image)
