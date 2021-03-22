x = lambda a : a + 10
print(x(5))

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Filter [0, 2, 4, 6, 8]
print(list(filter(lambda num: num %2 == 0, range(0,10))))

#Filter ['cabbage', 'chicken']
veg_list = ['tomato', 'cabbage', 'meat', 'chicken', 'goat']
print (list(filter(lambda word: word[0] == 'c', veg_list)))

### --- Pratique
## Equations
a = [1, 2, 3]
b = [1, 12, 11, 10]
c = [1, -4, 5, 9]

list(map(lambda x, y, z : 2*x + 3*y - 4*z, a, b, c ))


###  Expression Lambda

##--- Exemple 1---
##--- Changer la fonction suivante en expression lambda
def sayHello(message):
    print(message)

#solution:
sayHello("hello_1_avec_fonction")
sayHello= lambda m:print(m)
sayHello("hello_2_avec_expression_lambda")

#Functions evaluation
from math import sin, cos, tan, pi
def map_functions(x, functions):
    res = []
    for func in functions:
        res.append(func(x))
    return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))

#Solution lambda
mm = lambda x: map_functions(x, family_of_functions)
print(mm(pi))


# Cool *args
L1 = lambda *args : max(*args)
print(L1(4,3,9))
print(L1(3,5))
