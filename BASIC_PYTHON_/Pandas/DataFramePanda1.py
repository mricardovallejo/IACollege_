import pandas as pd

frame_list=pd.DataFrame([[2,4,6,7],[3,5,5,9]]) ## deux lignes et quatre colonnes
print(frame_list.head(4))  #il affiche le numero de lignes dans head, si rien default cest 5, pour afficher les premieres pour example

#   0  1  2  3
#0  2  4  6  7
#1  3  5  5  9


dico1={"RS" :["Facebook","Twitter","Instagram","Linkedin","Snapchat"],
       "Budget" :[100,50,20,100,50], "Audience" :[1000,300,400,50,200]}
frame_dico=pd.DataFrame(dico1)
print(frame_dico.head(4))

#    Audience  Budget         RS
#0      1000     100   Facebook
#1       300      50    Twitter
#2       400      20  Instagram
#3        50     100   Linkedin

frame_csv=pd.read_csv("salaires.csv")  #pour voir mon repertorire current use pwd
print(frame_csv.head(2))

#       nom  salaire  Age
#0    obama     4566   55
#1  michael     1000   34

salaires = frame_csv['salaire']
print(salaires)
print("max salaire: ", frame_csv['salaire'].max())

#0    4566
#1    1000
#2     345
#Name: salaire, dtype: int64

print(frame_csv['salaire']>1000)
#0     True
#1    False
#2    False
#Name: salaire, dtype: bool

