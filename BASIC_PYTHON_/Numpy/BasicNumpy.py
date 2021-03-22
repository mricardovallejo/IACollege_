import numpy as np

array_de_liste = np.array([1,3,2,4])
print(array_de_liste)

#[1 3 2 4]

array_range=np.arange(10)
print(array_range)

#[0 1 2 3 4 5 6 7 8 9]

vec =np.eye(5)
print(vec)

#[[1. 0. 0. 0. 0.]
# [0. 1. 0. 0. 0.]
#[0. 0. 1. 0. 0.]
#[0. 0. 0. 1. 0.]
#[0. 0. 0. 0. 1.]]

vec=np.ones(10)
print(vec)

#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

vec=np.ones((2,4))
print(vec)

#[[1. 1. 1. 1.]
# [1. 1. 1. 1.]]

#Same with zeros
vec=np.zeros(10)
vec=np.zeros((6,4))


a = np.random.randn(4)                   # loi normale centrée réduite
print(a)
#[-0.0977395   0.05488056 -1.20880019 -1.30066687]

b = np.random.random(size=(2,2))  # loi uniforme entre 0 et 1
print(b)
#[[0.16935549 0.31307799]
# [0.054125   0.08140167]]

rand_gen=np.random.RandomState(seed=12345)  #objet avec une graine fixée
print(rand_gen)
rand_gen2=np.random.RandomState(seed=12345)
print(rand_gen2)


np.random.seed(100)
arr = np.random.randint(0,100,10)
print(arr)
#[ 8 24 67 87 79 48 10 94 52 98]

print ( "max: " , arr.max())
print ( "min: " , arr.min())
print ( "avg: " , arr.mean())
print ( "minpos: " , arr.argmin())  #index de min value
print ( "maxpos: " , arr.argmax())  #index de max value
print ( "size: ", arr.shape)
print ( "typedata", arr.dtype) #int32


#max:  98
#min:  8
#avg:  56.7
#minpos:  0
#maxpos:  9

mat = np.arange(0, 20).reshape(2, 10)
print(mat)
#[[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 13 14 15 16 17 18 19]]

mat[0,1] #0
mat[:,0] #[0, 10]
mat[1,:] #[10 11 12 13 14 15 16 17 18 19]


#Import CSV but normally we use another module pour ca

#fichier = np.genfromtxt("data/data_numpy.csv", delimiter=",")

#fichier = np.genfromtxt("data/data_numpy.csv", delimiter=",", dtype="U75", skip_header=1)










