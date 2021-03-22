#Good Tricks
#-----------

# To avoid problems with names, user verbs for methods and nouns for attributes

import math

# Importing methods from another .py
from BasicPhyton.firstOne import table8 as minitable8


#Init methods default values
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#Init methode cool
def initMethodeCool(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
        print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

#Fibonnacci
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def main():

    #Print list tabbed
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))


    #Init Lists
    print( f(3, [2,4,6]) )
    print( f(4, [1, 43, 63]) )

    #Init methodes
    initMethodeCool("Limburger", "It's very runny, sir.",
        "It's really very, VERY runny, sir.", shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")

    # Init methodes
    n=7
    print ('Fibonnacci: ', fib2(n))

    # Antoher file methodes (firstOne.py)
    minitable8(5)  #See import: firstOne import table8
                   #If i import class with main, this main its executed,

    print('The value of pi is approximately {math.pi:.3f}.')

    #Iterators
    for element in [1, 2, 3]:
        print(element)
    for element in (1, 2, 3):
        print(element)
    for key in {'one': 1, 'two': 2}:
        print(key)

    #Secon iterator
    s = 'abc'
    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    


main()
