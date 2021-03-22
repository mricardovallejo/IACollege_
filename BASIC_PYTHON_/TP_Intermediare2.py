# Python de Base
## Octobre 8, 2020

#--- Exemple
# Ecrire du code pour demander a l utilisateur s il veut continuer ou sortir
# Solution 1
continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")

# Solution 2
continuer = "o"
while continuer == "o":
    print("On continue !")
    resultat = input("Voulez-vous continuer ? o/n ")
    if resultat != "o":
        break

# Solution 3 avec Python 3.8 uniquement
#while (continuer := "o") == "o":
#    print("On continue !")
#    if (resultat := input("Voulez-vous continuer ? o/n ")) != "o":
#        break

##-- Exemple

# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste
##(["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]

for i in range(0,len(liste)):
    if liste[i]=='Python':
        findit = i

liste.pop(findit)
list2= liste.append('Python')
print(liste)


# Supprimer le dernier element de la liste sans utiliser d index ni
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_pets2 = my_pets[:3]
print(my_pets2)

#1 mettre en majuscule les elements de la liste?

listex = ["Java", "Python", "C++"]
listey = []
for i in range(0, len(listex)):
     listey.append(listex[i].upper())

print(listey)

#Solution 2 - one ligne
b = [x.upper() for x in listex]
print(b)

#Solution 3
listex = ["Java", "Python", "C++"]
print ( list(map(lambda x: x.upper(), listex))) #!! Need list to knnow type of data deliver by map

#map(lambda x, y: x + y, numbers1, numbers2)


#solution
#1 Ecrire une fonctin pour inverser les elements de la liste?

my_pets3 = my_pets[::-1]
print(my_pets3)


### Modules

###-- pratique


##-- Écrire une fonction:
## 1) affiche les elements des deux listes
## 2) affiche la somme des elements de chaque liste
## 3) affiche le maximum valeur contenu dans chaque liste

import BasicPhyton.TP_Module as mymodule

list1, list2 = [123, 0, 4, 6], [1, 2, 3]

mymodule.sumlistes(list2, list2)
mymodule.maxlist(list2)
print(sum(list2))

## -- Programmation Fonctionnelle : Functions (map,filter, zip, reduce)

##--- Pratique
## Simplifier le code ci-dessous en utilisant la foncion map()

def mult_by_p(item):
    new_list=[]
    for i in item:
        new_list.append(i*2)
    return new_list
print(mult_by_p(my_list))

#solution

def myfunc(n):
    return n*2

my_list=[1, 2, 3]
x5 = map(myfunc, my_list)
print(list(x5))


## --- Pratique
## Simplifier le code ci-dessous en utilisant la foncion map()
def capitalize(string):
    return string.upper()

## solution
list_pets = ['perro', 'gato']
print(list(map(capitalize, list_pets)))


##--- Exemple

# 1) Filtrer les scores superieures a 50 en utilisant la fonction filter ?
# 2) Filtrer les scores superieures entre 50 a 90 en utilisant la fonction filter ?
# 3) Filtrer les scores superieures entre 100 en utilisant la fonction filter et afficher un message si le resultat est vide?

## solution 1)
scores = [73, 20, 65, 19, 76, 100, 88]
def is_smart_student(score):
    return score > 50

def is_student_50_90(score):
    return score > 50 and score < 90

def is_student_plus_100(score):
    return score > 100

print(list(filter(is_student_50_90, scores)))

a1 = list(filter(is_student_plus_100, scores))
if len(a1)>0:
    print(a1)
else:
    print("Error")

##--- Pratique
## Simplifier le code ci-dessous en utilisant la foncion filter()
my_list=[1, 2, 3, 9, 39]

def verif_si_dev_3(item):
    res=[]
    for i in item:
        if i%3==0:
            res.append(i)
    return res

res=verif_si_dev_3(my_list)
print(res)

## solution
def verif_si_dev_3(item):
    return item %3 == 0

my_list = [3, 6, 9, 7]
print(list(filter(verif_si_dev_3, my_list)))


##--- Exemple

# Rassembler deux listes dans une liste de tuples, et trier les nombres par ordre croissant puis par ordre decroissant
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
# Modifier le code pour rassembler n listes ?

## indication : sorted() fonction pour trier
## sorted(iterable, key, reverse=False)
## sorted(Liste ou Set ou Tuple ou Dictionnaire, reverse = True) ou sorted(Liste, reverse = False)
## sorted(Liste, key = len))

##nom_list.sort(key, reverse=False)
# sort ne retourne pas de resultat,

## solution
##print(list(zip(my_strings, sorted(my_numbers))))

#TODO

##--- Pratique
## Creer une liste de tuple en utilisant la fonction zip pour les trois listes suivantes

list_numero_tel =['514-234-3423','514-234-1000', '514-100-1020','650-234-1000']
list_nom_personnes =['spider-man','batman','joker']
list_pays=['Montreal','Boston', 'New-york']

## solution
a=list(zip(list_numero_tel, list_nom_personnes,list_pays))
print(a)
print(len(a)) #3 elements

#Solution
import functools  ## module de la programmation fonctionnelle
print(dir(functools)) #( pour voir ce qu il ya dans le module)

##--- Exemple
## utiliser la fonction reduce pour donner le nombre d'heures totales travaillees pendant toute la semaine
## solution
from functools import reduce
travail_chaque_jour_semaine=[8, 5, 6,10, 14]
def func(accum,item):
    print(accum, item)
    return accum + item

# ExplicationL: reduce(function, sequence, valeur_initial)
print((reduce(func,travail_chaque_jour_semaine, 0)))


##--- Pratique
## utiliser la fonction reduce pour donner la quantite de produits consommer pendant les mois de janvier et fevrier?
## sachant que pour les autres mois de l annee la quantite est de 100kg????? TODO only part2
from functools import reduce
qtes_produits_mois_janvier = [73, 20, 65, 19, 76, 100, 88]
qtes_produits_mois_fevrier= [50,46,32,20,10]

## solution
def accumulator(acc, item):
    #print(acc, item)
    return acc + sum(item)
print(reduce(accumulator, (qtes_produits_mois_janvier, qtes_produits_mois_fevrier), 0))


### --- Pratique
## Enonce: le code suivant a un probleme. ameliorer le pour indiquer que le calcul ne s est pas fait sur tous les elements
##de la liste
## indication avec if elif else
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


##--- Exemple 2---
##--- Changer la fonction suivante en expression lambda
def sommer(p1,p2):
    return p1+p2

## solution
print("avec fonction: "+ str(sommer(23,24)))
somme =lambda p1,p2: p1+p2
print("avec expression lambda: "+str(somme(23,24)))


##--- Exemple 3:
# le module random permet de generer des nombres aleatoire
# randint(a,b): renvoie un entier choisi aleatoirement dans [a,b] avec randrange(a, b+1)
# random():renvoie un flottant choisi dans l'intervalle [0;1]
# uniform :renvoie un flottant choisi dans l'intervalle[a;b]

import random
print('---------')
print("exemple random(): "+str(random.random()))
print("exemple uniform(): "+str(random.uniform(2.5, 10.0)))
print('---------')
#--Écrire une lambda expression qui génère un nombre aléatoire (soit 4, 5,6)

nbre_aleatoire =lambda a,b:random.randint(a,b)
print("nombre aleatoire genere entre 4,5,6 est: " +str(nbre_aleatoire(4,6)))
random.seed(a=None, version=2)
print("nombre aleatoire genere entre 4,5,6 est: " +str(nbre_aleatoire(4,6)))
random.seed(a=None, version=2)
print("nombre aleatoire genere entre 4,5,6 est: " +str(nbre_aleatoire(4,6)))


##----------#--Écrire une lambda expression qui génère une probabilite de valeurs entre 20% et 80%?

#TODO

### ---- Pratique
## Ecrire un code qui genere deux nombres aleatoires et indique a l utilisateur lequel
## des deux nombres est le plus grand

r= random.uniform(2.5, 10.0)
print('r: ',r)
s= random.uniform(2.5, 10.0)
print('s: ',s)
if (r>s):
    print ('r = {} es mayor que {}'.format(r,s))
else:
    print ('r = {1} es mayor que {0}'.format(r,s))


    ############################################################################

### ---- Pratique
#--Écrire une lambda expression qui affiche la plus grande valeur de deux nombres?
L1 = lambda x,y : max([x, y])
print(L1(4,3))
print(L1(3,5))


#--Écrire une lambda expression qui affiche la plus grande valeur de trois nombres?
L1 = lambda *args : max(*args)
print(L1(4,3,9))
print(L1(3,5))
print(L1(3,5,6,4,3,8,3))

#--Écrire une lambda expression qui permet de classer deux nombres par ordre croissant?

listNoms = ['Pedro', 'Zeus', 'Swhwachesxnneger', 'Madonna']
listNoms.sort()
print(listNoms)

#Solutcion 1
listNoms.sort(reverse=True)
print(listNoms)

#Solucion 2
def myFunc(e):
    return len(e)  #Length comme sort methode

listNoms.sort(key=myFunc)
print(listNoms)

listNoms.sort(key=myFunc, reverse=False)
print(listNoms)


#--Écrire une lambda expression qui permet de calculer la valeur absolue d’un parametre?
L2 = lambda x: abs(x)
print(L2(-30))


#-- Écrire une lambda expression qui permet de mettre en majuscule les elements de la liste?
listNoms = ['Pedro', 'Zeus', 'Swhwachesxnneger', 'Madonna']
L1 = list(map(lambda x: x.upper(), listNoms))
print(L1)

#-- Écrire une lambda expression qui permet d inverser les elements de la liste?
listNoms = ['Pedro', 'Zeus', 'Swhwachesxnneger', 'Madonna']


## -----------
#--  Écrire une lambda expression qui permet de calculer la somme des n premiers nombres entiers
#--  positifs  ( proposer deux versions ):
#--  version 1:  Somme = N + (N-1) + (N-2) + …+ 2+1

#Solucion 1
import functools
list_of_nums = [2,4, 6, 2, 9]
print(functools.reduce(lambda x, y: x + y, list_of_nums))

#Solucion 2
import functools
leNum = 8                        #[1 3 5 7]==>16
only_odd = [num for num in list(range(leNum)) if num % 2 == 1]
print(functools.reduce(lambda x, y: x + y , only_odd))


## -----------
#-- Écrire une lambda expression permet d’afficher les n termes de nombres
#-- naturels impairs et leur somme. Ce programme aura pour entrées

leNum = 8                        #[2 4 6]==>12
only_pair = [num for num in list(range(leNum)) if num % 2 == 0]
print(functools.reduce(lambda x, y: x + y , only_pair))



###  Expression Lambda avec les fonctions map, filter, zip and reduce

## --- Pratique
## utiliser l expression lambda et la fonction reduce pour donner le nombre d'heures totales
## travaillees pendant toute la semaine

## -- Simplifier le code ci-dessous
travail_chaque_jour_semaine=[8, 5, 6,10, 14]

print("solution avec fonction")
def func(accum,item):
    return accum + item
#reduce(function, sequence, valeur_initial)
print((reduce(func,travail_chaque_jour_semaine, 0)))

## solution 1
print("solution 1 avec lambda expression")
func =lambda accum, item: accum+item
print((reduce(func,travail_chaque_jour_semaine, 0)))

## solution 2
print("solution 2 avec lambda expression")
print((reduce(lambda accum, item: accum+item,travail_chaque_jour_semaine, 0)))



## --- Pratique
## Simplifier le code suivant avec lambda expression. Proposer un menu a l utilisateur. s il choisit sin, appeler la fonction sin
##   ect...
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

##--- Solution

## Corriger le code ci-dessous
class Chien:
    def __init__(self, race):
        self.race = race

    @property
    def taille(self):
        return 100

class Chihuahua(Chien):
    def __init__(self, nom):
        self.nom = nom


mychien = Chihuahua("Lily")
mychien.race = 'Labrador'
print('Le chien {} race {} a un taille {} cms'.format(mychien.nom, mychien.race, mychien.taille))


## ---- Exemple ?? TODO
## Que remarquez vous dans ce code?
class this_is_class:
    def show(in_place_of_self):
        print("Collecte et stockage de donnees ")

object = this_is_class()


##--- Pratique
# La classe Etudiant hérite de la classe Personne.
# La classe Professeur hérite de la classe Employé et la classe Employé hérite de la classe Personne.
# Un Etudiant est une Personne.
# Un Professeur est un Employé et un Employé est une Personne.
# Travail à faire 
# Ecrire du code pour les classes
# Chaque classe doit contenir un constructeur d'initialisation.
# Creer : 1) deux objets étudiants 2) deux objets employés 3) deux objets professeurs.
# 4) afficher les informations de chaque personne. 


class Personne:
    def __init__(self, nom):
        self.nom = nom

class Chercheur(Personne):
    def __init__(self, tr):
        self.theme_recherche=profession


class Etudiant(Personne):
    def __init__(self, numero_etu):
        self.numero_etu=numero_etu


class Enseignant(Chercheur, Etudiant):
    def __init__(self, cours):
        self.cours=cours

class Employe(Personne):
    def __init__(self, numero_empl):
        self.numero_empl=numero_empl

class Professeur(Employe):
    def __init__(self, numero_prof):
        self.numero_prof=numero_prof

e1= Etudiant("e1")
e2 = Etudiant("e2")

empl1 = Employe("EMP1")
empl1.nom = 'Ricardo'

empl2 = Employe("EMP2")
empl2.nom = 'Erika'


prof1 = Professeur("P1")
prof1.nom = "Pedro"
prof1.empl = "E001"
prof1.numero_prof = "P001"

prof2 = Professeur("P2")
prof2.nom = "Juana"
prof2.empl = "E002"
prof12numero_prof = "P002"

print ("Le professeur {} a No employe {} et No Prof: {}".format(prof1.nom, prof1.empl, prof1.numero_prof))
print ("Le professeur {} a No employe {} et No Prof: {}".format(prof2.nom, prof2.empl, prof2.numero_prof))
print ("Le employe {} a code {}".format(empl1.nom, empl1.numero_empl))
