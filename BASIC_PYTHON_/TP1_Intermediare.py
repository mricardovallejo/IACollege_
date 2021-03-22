#Exemple
#Remplacer un élément dans une liste
liste = ['Obama', 'Michelle', 'Spider-man', 'Mickey', 'Hulk']
nom_a_chercher = 'Mickey'
nouveau_nom = 'Mini'

def replaceList(newMot, targetMot):
    for i in range(len(liste)):
        if liste[i] == targetMot:
            liste[i] = newMot

    print(liste)

replaceList(nouveau_nom, nom_a_chercher)

#Solution 2
resultListe = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
print(resultListe)

##-----Pratique -----:
def cube(n):
    return n**3

print('cubo: ', cube(2))

#créer une expression lambda qui calcule le cube d'un nombre donné?
w = lambda z : z**3
print('cubo lambda: ', w(2))

#Ecrire du code pour additionner deux variables

myadd= lambda a,b : a+b
print( 'addition', myadd(10,20) )


#créer une expression lambda qui retournera oui si le nombre donné est pair et
#non si le nombre donné est impair?
m=23
l= lambda x: 'YES' if m%2==0 else 'NO'
print(l(4))

#Ecrire du code simple pour multiplier chaque element de la liste par 2
#indication: expression lambda et map()
lst=[2,3,4,5]
#créer une expre
result = list(map(lambda n:n*2,lst))
print('list x 2: ', result)
print('list original: ', lst)

#Ecrire du code simple pour recuperer uniquement les elements de la liste qui sont divisible par 2
#indication: expression lambda et filter()

lst=[10,2,33,45,89,2]

result = list(filter(lambda x:x%2==0,lst))
print('Filtered list: ', result)
for i in result:
    print(i)

#Ecrire du code simple pour aditionner les elements d une liste un a un
#indication: expression lambda et reduce

import functools

lst2=[5,10,15,20]
result2 = functools.reduce(lambda x,y : x+y, lst2)
print('sume elements: ', result2)


#Exemple
#Trier une liste de tuples
listeTuples = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
listeTuples.sort(key=lambda x: x[1])
print(listeTuples)


#-------Pratique / Solution
#Écrire un programme qui définit la classe Employee avec les attributs suivants:
#nom, (courriel) email  et la méthode changer_courriel()
# verifier si le courriel est bin formate et le nom n’est pas vide

class Employe:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @name.setter
    def name(self, name):
        if name:
            self.__name = name
        else:
            print ('Name cant be empty')

    @email.setter
    def email(self, email):
        if email:
            if (email.find('@') == -1 | email.len < 2):
                print ('Mail format its not correct')
            else:
                self.__email = email
        else:
            print ('mail cant be empty')

emp1 = Employe
emp1.name = 'Ricardo Vallejo'
emp1.email = 'mricardov@hotmail.com'

print('Employe mail: {1} avec nom {0}'.format(emp1.name, emp1.email))

emp2 = Employe
emp2.name= 'x' #TODO Ca ne marche pas la validation
print(emp2.name)


#-------Pratique / Solution
#------Écrire un programme qui définit une classe Téléphone avec les attributs privés numéro et modèle
#---Ajouter au programme de la question 7) les méthodes getnumero et setnumero

class telephone ():
    def __init__(self, numero, modele):
        self.__numero = numero
        self.__modele= modele

    def getNumero(self):
        return self.__numero

    def setNumero(self):
        self.__numero= numero

