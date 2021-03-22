import numpy as np
## -- Numpy et Pandas ( october 20/10/2020)

## --- pratique 1:
## construire un vecteur avec [3,4,5,6]
## assigner resultat a la variable vector
## indice : np.array([3,4,5,6])

import numpy as np
array_de_liste = np.array([3,4,5,6])
print(array_de_liste)


## --- pratique 2:
## construire une matrice  depuis la liste de listes [[2,5,15],[20,50,50],[34,99,45]]
## Afficher les resultats
## assigner le resultat a la variable matrix

import numpy as np
array_de_liste = np.array( [ [77, 88, 99] , [31,42,63] , [11,22,33]])
print(array_de_liste)

## --- pratique 3:
## Donner la taille du tableau [1,2,3,4]suivant puis changer sa taille
## Afficher les resultats
## indication : shape, reshape

import numpy as np
array_de_liste = np.array([1,2,3,4])

print(array_de_liste.shape)
#(4,)


reshaped = array_de_liste.reshape(2,2)
print(reshaped)
#[[1 2]
# [3 4]]

print(reshaped.shape)
#(2, 2)


## --- pratique 4:
## Donner la taille de la matrice [[5,10,15], [20,25,30], [40,45,50]] suivant puis changer sa taille
## Afficher les resultats
## indication : shape, reshape

import numpy as np

array_de_liste = np.array( [ [5,10,15], [20,25,30], [40,45,50] ])

print(array_de_liste.shape)
#(3, 3)

reshaped = array_de_liste.reshape(1,9)

print(reshaped)
#[[ 5 10 15 20 25 30 40 45 50]]

## --- pratique 5:
## Executer le code suivant ( en specifiant le path du fichier)
#import numpy as np
#fichier = np.genfromtxt("data_numpy.csv", delimiter=",")
## Utiliser les fonctions type() et print() pour afficher le type de fichier



import numpy as np
fichier = np.genfromtxt("C:/wrkOrion3/IACollege/Numpy/salaires.csv", delimiter=",")
print(fichier)
print(fichier.dtype)
#float64


## --- pratique 6:
## creer un vecteur random ayant 4 valeurs

a = np.random.randn(4)
print(a)

## creer une matrice random de taille (2X2)

b = np.random.random(size=(2,2))
print(b)

## --- pratique 7:
# creer un vecteur depuis la liste[1, 2, 3, 4] et afficher son type
##solution
import numpy as np
numbers=np.array([1, 2, 3, 4])
print(numbers.dtype)


## --- pratique 8
## Afficher toutes les lignes des 2 premières colonnes de data_numpy à la variable first_two_columns.
# Afficher les 10 premières lignes de la première colonne de data_numpy à la variable first_ten_years.
# Afficher les 10 premières lignes de toutes les colonnes de data_numpy à la variable first_ten_rows.
# Afficher les 20 premières lignes des colonnes d'indice 1 et 2 de data_numpy à la variable first_twenty_regions.

## solution

import numpy as np

#data_numpy = np.genfromtxt("C:/wrkOrion3/IACollege/Numpy/data_numpy.csv", delimiter=",")  Ca marche!!
data_numpy = np.genfromtxt("data_numpy.csv", delimiter=",")
print(data_numpy)

first_two_columns = data_numpy[:,0:2]
print(first_two_columns )
first_ten_years = data_numpy[0:10,0]
print(first_ten_years)
first_ten_rows = data_numpy[0:10,:]
print(first_ten_rows)
first_twenty_regions= data_numpy[0:20,1:3]
print(first_ten_rows)


## --- pratique 9
#Importer la librairie pandas.
#Utiliser la fonction pandas.read_csv() pour lire le fichier "food_info.csv"
#Utiliser les fonctions type() et print() pour afficher le type de food_info
#solution

import pandas as pd
food_info = pd.read_csv("C:/wrkOrion3/IACollege/Numpy/data_numpy.csv")
print(food_info)
print(type(food_info))

#[3257 rows x 4 columns]
#<class 'pandas.core.frame.DataFrame'>



##--- pratique 10
#Afficher la 1000e ligne du dataframe food_info
#solution
row_1000 = food_info.loc[999]
print(row_1000)


##--- pratique 11
#Assigner la colonne "protein_(g)" à la variable protein.
#Assigner la colonne "Cholestrl_(mg)" à la variable cholesterol.
#Afficher les résultats.

## solution
protein = food_info["Protein_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]


##--- pratique 12
#Sélectionner les colonnes 'Shrt__Desc', 'Selenium_(mcg)' et 'Thiamin_(mg)'
#et assigner le dataframe résultant à la variable selenium_thiamin.
#Afficher le résultat.

## solution
selenium_thiamin = food_info[['Shrt_Desc', 'Selenium_(mcg)', 'Thiamin_(mg)']]
print(selenium_thiamin)

## --- pratique 13
# 1) Sélectionner et afficher seulement les colonnes qui utilisent comme unité de mesure les grammes
#(c'est à dire qui se terminent par "(g)"). Pour cela:
#Utiliser l'attribut columns pour retourner le nom des colonnes du dataframe food_info
#et convertir en liste utilisant la méthode tolist()

## 2) Créer une nouvelle liste qu'on nommera gram__columns, contenant seulement les colonnes se terminant
##  par "(g)". Indice: la méthode endswith() retourne True si l'objet sur lequel on l'applique se termine
## par l'élément entre parenthèses. ex: total_(g).endswith("(g)") retourne True. Une boucle for est fortement conseillé pour parcourir tous les noms de colonne.

## 3) Sélectionner les colonnes de gram_columns pour le dataframe food_info et assigner le dataframe résultat
## à la variable gram_df

## 4) Afficher les 3 premières valeurs de ce dataframe gram_df

## solution
##col_names = food_info.columns.tolist()
##gram_columns = []

##for c in col_names:
##  if c.endswith("(g)"):
##     gram_columns.append(c)

##gram_df = food_info[gram_columns]

##gram_df.head(3)



##--- pratique 14
#Lire le dataset 'fandango_score_comparison' dans le dataframe fandango.
#Retourner un DataFrame contenant seulement la première et la dernière ligne et assigner le résultat à la variable first_last.
#Afficher le résultat.

###--- solution
#import pandas as pd
#fandango = pd.read_csv('fandango_score_comparison.csv')
#first = 0
#last = fandango.shape[0] - 1
#first_last = fandango.iloc[[first,last]]
#first_last


##--- pratique 15
#Lire le fichier "fandango_score_comparison.csv" dans un dataframe qu'on nommera fandango.
#Afficher les 2 premières lignes de fandango.

## solution
##import pandas as pd
##fandango = pd.read_csv('fandango_score_comparison.csv')
##fandango.head(2)

##---- pratique 16
##Sélectionner la colonne "FILM" et assigner la à la variable series_film puis afficher les 5 premières valeurs.
#Faire de même avec la colonne "RottenTomatoes" et assigner la à la variable series_rt puis afficher les 5 premières valeurs.

## solution
##series_film = fandango['FILM']
##print(series_film[0:5])
##series_rt = fandango['RottenTomatoes']
##print(series_rt[0:5])


###--- pratique 17
##Créer un objet Series qu'on nommera series_custom qui aura
##un index de chaines de caractères (basé sur le nom des films
##qu'on assignera à la variable film_names) et contiendra toutes
##les notes RottenTomatoes de series_rt qu'on assignera à la variable rt_scores.

## solution
# importer l'objet Series depuis pandas
#from pandas import Series

#film_names = series_film.values
#rt_scores = series_rt.values
#series_custom = Series(rt_scores, index=film_names)


###--- pratique 18
##Créer la liste original_index contenant l'index actuel à partir de l'attribut index.
##Trier cet index en utilisant la méthode sorted() et assigner le résultat à la variable sorted_index.
##Puis appliquer la méthode reindex() à notre Series custom_series afin de réindexer selon l'index de sorted_index.
##Stocker le résultat dans la variable sorted_by_index.
##Afficher le résultat.

## solution
##original_index = series_custom.index
##sorted_index = sorted(original_index)
##sorted_by_index = series_custom.reindex(sorted_index)
##print(sorted_by_index)


###--- pratique 19
##Trier la Series series_custom par index en utilisant la méthode sort_index() et assigner le résultat à la variable sc2.
##Trier la Series series_custom par valeurs et assigner le résultat à la variable sc3.
##Afficher les 10 premières valeurs de sc2 et sc3.

## solution
##sc2 = series_custom.sort_index()
##sc3 = series_custom.sort_values()
##print(sc2[0:10])
#print(sc3[0:10])

###--- pratique 20
##Assigner à la variable criteria_one le critère des valeurs de series_custom supérieurs à 50.
##Assigner à la variable criteria_two le critère des valeurs de series_custom inférieurs à 75.
##Retourner un nouvel objet Series filtré qu'on nommera both_criteria qui contient seulement les valeurs pour lesquelles les 2 critères sont vrais.
##Afficher ce dernier résultat.

##-- solution
##criteria_one = series_custom > 50
##criteria_two = series_custom < 75
##both_criteria = series_custom[criteria_one & criteria_two]
##both_criteria



