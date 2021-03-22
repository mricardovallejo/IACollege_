#1-2  Function avec arguments
import math

def carre(a):
    return print('Carre: ', a*a)

def sum1(a,b):
    return print('Response 1-2 sum: ', (a**2)+(b**2))

def mult1(a,b):
    return print('Response 1-2 mult: ', (a**2)*(b**2))

def div1(a,b):
    if(b!=0):
        return print('Response 1-2 div  : ', (a**2)/(b**2))

# 3-4

def cubo(a):
    return print('cubo: ', a*a*a)
def sum2(a,b):
    return print('Response 3-4 sum: ', (a**3)+(b**3))

def mult2(a,b):
    return print('Response 3-4 mult: ', (a**3)*(b**3))

def div2(a,b):
    return print('Response 3-4 div: ', (a**3)/(b**3))

# 1-2-3-4 meme methode

def combine1(a, mypower):
    return a**mypower
def sum3(a,b, mypower):
    return print((a**mypower)+(b**mypower))

def mult3(a,b, mypower):
    return print((a**mypower)*(b**mypower))

def div3(a,b, mypower):
    return print((a**mypower)/(b**mypower))

#5 Function recursives  :(

def recur1(n):
    print(str(n))
    if n == 1:
        return 1
    else:
        return n+recur1(2*n-1)

    print("La sum recursive: " , recur1(n))

#6

def multi2lists(x,y):
    if len(x) == len(y):
        s=[]
        for i in range (0 , len(x)+1):
            s.append( x[i]*y[i] )
        return print(s)
    else:
        print ("Not possible")

#7



def table8(limite):
    limite = int(input('Introduce the limit: '))
    for i in range(0, limite):
            print(8, " x ", i, "= ", 8*i)

def main():

    a=5
    b=6

    print('MENU\n')
    print('A. Excersice 1-2\n')
    print('B. Excersice 3-4\n')
    print('C. Excersice 5\n')
    print('D. Excersice 6\n')
    print('E. Excersice 7\n')
    print('E. Excersice 8\n')
    option = input(' Option? : ').upper()

    if option == 'A':
        carre(a)
        sum1(a, b)
        mult1(a, b)
        div1(a, b)
    elif option == 'B':
        cubo(a)
        sum2(a, b)
        mult2(a, b)
        div2(a, b)
    elif option == 'C':
        combine1(a, 2)
        sum3(a, b, 2)
        mult3(a, b, 2)
        div3(a, b, 2)
    elif option == 'D':
        n = 5
        recur1(n)
    elif option == 'E':
        x = [1, 2, 3]
        y = [2, 4, 6]
        multi2lists(x, y)
    elif option == 'F':
        limite = 10
        table8(limite)

#This is good when firstOne.py will be called from another .py but firstOne.py has main()
#Only execute main when is run not when its loaded.
if __name__ == "__main__":
    main()


