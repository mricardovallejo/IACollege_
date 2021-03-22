#!/usr/bin/env python
# coding: utf-8

# # Rappel Python de Bases + Programmation Orientée Objet

# ###Section A : Débutant


###Conversion


##-----Pratique -----:

# 1. Convertir le nombre en chaînes de caractères

# Solution 1 for input data
n = str(input('Enter a number:'))

# Solution 2 for output data # https://pyformat.info/
n2 = input('Enter a number:')
print('Le number est: {:_<10s}'.format(n2))
print('Le number est: {: <15s}'.format(n2))

#-------------

#Exemple 2:

def echange2(a, b):
    c=a
    a=b
    b=c
    return a,b

x,y = 2,3
x,y=echange2(x,y)
print("x=",x)
print("y=",y)

##-----Pratique -----:
# La fonction echangeab() ne fonctionne pas.

def echangeab():
    global a
    global b
    c=a
    a=b
    b=c
    return a, b

a=20
b=30
echangeab()
print("a=", a)
print("b=", b)

##-----Pratique -----:
# Ecrire une fonction qui appelle une autre fonction

def mt_Km(mt):
    return mt / 1000

def mt_cm(mt):
    return mt * 100

def conversion():
    x = int(input("Input meters: "))
    tox = str(input("Target length unit")).upper()

    if (tox == 'KM'):
        print (' {} mt  ==> {:3f} Km '.format(x, mt_Km(x)))
    elif (tox == 'CM'):
        print (' {} mt  ==> {:3f} Km '.format(x, mt_cm(x)))
    else:
        print ('Invalid option')

conversion()


#Exemple:
#Créer une liste de nombres allant de 5 à 15
print(list(range(5,16)))
[5,6,7,8,9,10,11,12,13,14,15]

#Example
ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])
print(ma_liste[-1])
print(ma_liste[:2])
print(ma_liste[-2:])

##-----Pratique -----:
#--Créer une liste de nombres pairs de 1 à 100
ma_liste2 = list(range(0,101,2))
print('pairs: ', ma_liste2[-50:])
print('pairs: ', ma_liste2[1:50+1])


##-----Pratique -----:
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## Récupérer un élément sur deux dans la liste ?
## Récupérer un élément sur quatre dans la liste ?
## indication: ma_liste[indice_de_depart:indice_de_fin:pas]


## Solution
## Récupérer un élément sur deux dans la liste ?
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## solution 1
#pas besoin d'indiquer d'indice spécifique pour les deux premiers nombres
print(ma_liste[::2])
## solution 2
print(ma_liste[0:10:2])
## solution 1
print(ma_liste[::4])
## solution 2
print(ma_liste[0:10:4])

#Exemple
#------Ajouter une élément dans une liste
ma_liste = [1, 2, 3]
ma_liste.append(5)
print('append: ', ma_liste)

#Exemple:
#Récupérer les éléments communs aux deux listes
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
sliste_01 = set(liste_01)
sliste_02 = set(liste_02)
intersect = sliste_01.intersection(sliste_02)
print('element commons: ', list(intersect))

#Solution
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
sliste_01 = set(liste_01)
sliste_02 = set(liste_02)
uni = sliste_01.union(sliste_02)
print('ALL ELEMENT NON REPEATED', list(uni))

