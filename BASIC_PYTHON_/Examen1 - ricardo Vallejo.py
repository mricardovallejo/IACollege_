#Examen: Ricardo Vallejo

#1)

def myString():
    return 'hi'

def useString():
    x = myString() + ' Ricardo'
    print(x)

useString()

#3)

import numpy as np
my_list = [3,4,10,6, 6,45,54]
my_array = np.array(my_list)
print(my_array)

my_list2 = [6,7,17,6, 7,4,5]
my_array2 = np.array(my_list2)
print(my_array2)

matrix = np.array([my_array, my_array2])
print(matrix)

#4)

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    return a_set & b_set


a = [1, 2, 3,4, 5, 6, 7, 9, 10, 11, 12,13,14,15,16,17,18]
b = [2, 3, 5, 6, 8, 10, 12, 14]
commns = common_member(a, b)
print(commns)

result = list(filter(lambda x: (x > 5), commns))
print(result)


#5)
newArray=[]
for element in ["Obama", "Michelle", "Spider-man", "Mickey", "Hulk", "Monsieur" ]:
    if element[0] == "M" or element[0] == "H":
        newArray.append('V')
    else:
        newArray.append(element)

print(newArray)

#6
newArray2=[]
for element in [10,2,33,45,89,2, 40]:
    if element%4 == 0:
        newArray2.append(element)
    else:
        print("Non divisible")

print(newArray2)

#8)

myIndex = int(input("Enter index to recover:"))
print(myIndex)
myList = [10,2,33,45,89,2, 40]

if (myIndex < 0 or myIndex > len(myList)):

    resultx = myList[myIndex]
else:
    print("Error Index")

print(resultx)







#QUESTION 10 point PYTHON
import re
mot = input("Enter mot:")
lenghtmot = len(mot)
print(lenghtmot)

x = re.findall("[aeiouAEIOU]", mot[0])

if x:
    print ("commence pour voylle")
else:
    print ("ne commence pas pour voyelle")

