
class Polynomial:

    def __init__(self, *coefficients): #?? *
        self.coefficients = coefficients[::-1]

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res

# a constant function
p1=Polynomial(1,1,10) #Create polynomial (1,1,10) ==> x^2+x+10  #Using __initi__ constructor
for i in range(1, 10): #Evaluate multiple times polynomial
    print(i, p1(i)) #Using _call__

# a third degree Polynomial
p3 = Polynomial(1, -0.5, 0.75, 2)

