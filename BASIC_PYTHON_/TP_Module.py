
##-- Écrire une fonction:
## 1) affiche les elements des deux listes
## 2) affiche la somme des elements de chaque liste
def sumlistes(lista, listb):
    res_list=[]
    for i in range(0, len(lista)):
        res_list.append(lista[i] + listb[i])
    print(res_list)


## 3) affiche le maximum valeur contenu dans chaque liste
def maxlist(lista):
    print( max(lista) )

def sumlistx(lista):
    print(sum(lista))

