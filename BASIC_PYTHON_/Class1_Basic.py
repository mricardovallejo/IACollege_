#Basic knowledge
#---------------

#4: variable de type String et print
X = "String"
print(X)

#5: variable de type String et format 
# format : permet d’afficher un chiffre avec une chaîne en utilisant placeholders.
name = 'Obama'
number = 30
print('My name is {} and my number is {}'.format(name, number))
print('My name is {one} and my number is {two}'.format(one=name, two=number))
print('My name is {one} and my number is {two}, {one} again and {two} again'.format(one=name, two=number))

#6: les éléments d’une chaîne sont stockés et récupérés par leur position relative 
X = "String"
print(X[0])          # premier élément
print(X[-1])         # dernier élément
print(X[1:])         # tout après  l’index 1
print(X[:4])         # tout depuis 0 jusqu’4 sans inclure le quatre
print(X[0:4])       # tout depuis 0 jusqu’4 avec inclusion du quatre

# 7:
st1 = "python"
st2 = "scripting"
st3 = st1 + st2
print(st3)

# 8:
str = "python"
print(str.startswith("p"))
print(str.endswith("on"))
print(str.islower())
print(str.isupper())
print(str.isalpha())
str = "5678903456"
str.isnumeric()

# 9: méthode:Join
x = "python"
y = "-".join(x)
print(y)
print("*".join(x))
print("\t".join(x))
print("\t".join(x))
print("\n".join(x))

# 7: st1 = "python"  
st2 = "scripting"
st3 = st1 + st2
print(st3)

# 8: str = "python"  
print(str.startswith("p"))
print(str.endswith("on"))
print(str.islower())
print(str.isupper())
print(str.isalpha())
str = "5678903456"
str.isnumeric()

# 9: méthode:Join

x = "python"
y = "-".join(x)
print(y)
print("*".join(x))
print("\t".join(x))
print("\t".join(x))
print("\n".join(x))

#12: strip()
x='Python   '
print(x.strip())

# 13:

x = 'Python is easy and is popular   '
print(x.count('is'))
print(x.find('y'))
print(x.find('p', 23))
print(x.index('p', 10))

# 14:
str = input("Enter your String:")
print(str.center(3))
print(str.ljust(3))
print(str.rjust(3))

#CONDITIONS
#Exemples de codes:
# 1:
if 3 > 2:
    print('True')

# 2:
if 3 != 2:
    print('True')
else:
    print('False')

# 3:
if 1 == 2:
    print('1st statement')
elif 2 == 2:
    print('2nd statement')
else:
    print('3rd statement')
# 4:
if 1 == 2:
    print('1st statement')
elif 3 == 3:
    print('2nd statement')
elif 2 == 2:
    print('3rd statement')
else:
    print('4rd statement')
