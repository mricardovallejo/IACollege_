import pandas as pd
import numpy as np
# importer le data dans le dataframe
tit = pd.read_csv("titanic.csv")
print(tit.head(3))
#survived  pclass     sex   age  sibsp  parch     fare embarked deck
#0         0       3    male  22.0      1      0   7.2500        S  NaN
#1         1       1  female  38.0      1      0  71.2833        C    C
#2         1       3  female  26.0      0      0   7.9250        S  NaN

# Condition
# rechercher les enregistrement ayant sex = male
tit.sex="male"
print(tit.sex)

#0      male
#1      male
#2      male
#3      male
#4      male

print("Choix 1: ")
print(tit[tit.sex=='male']['fare'])

#0        7.2500
#1       71.2833
#2        7.9250
#3       53.1000

print("Choix 2: ")#==>Recomendnde
print(tit.loc[tit.sex=='male','fare'])

#0        7.2500
#1       71.2833
#2        7.9250
#3       53.1000

# Condition : mask pour avoir les colonnes de type object =string
print("A: ")
object = "String"
print(tit.dtypes == object)


#A:
#survived    False
#pclass      False
#sex         False
#age         False
#sibsp       False
#parch       False
#fare        False
#embarked    False
#deck        False
#dtype: bool

print("B: ")
print(tit.dtypes)

##B:
#survived      int64
#pclass        int64
#sex          object
#age         float64
#sibsp         int64
#parch         int64
#fare        float64
#embarked     object

# Condition : mask : afficher que les colonnes de types numériques
print("C: ")
mask = tit.dtypes==object
print(mask)

#C:
#survived    False
#pclass      False
#sex         False
#age         False
#sibsp       False
#parch       False
#fare        False
#embarked    False
#deck        False
#dtype: bool


print(tit.loc[:,~mask])

#survived  pclass   sex   age  sibsp  parch      fare embarked deck
#0           0       3  male  22.0      1      0    7.2500        S  NaN
#1           1       1  male  38.0      1      0   71.2833        C    C
#2           1       3  male  26.0      0      0    7.9250        S  NaN
#3           1       1  male  35.0      1      0   53.1000        S    C
#4           0       3  male  35.0      0      0    8.0500        S  NaN
#5           0       3  male   NaN      0      0    8.4583        Q  NaN
#6           0       1  male  54.0      0      0   51.8625        S    E


# Est-ce qu il y avait sur le titanic des passagers males et ayant plus que 14 ans, qui ont survécu?
mask_1 = tit.sex =='male'
mask_2 = tit.age >14
print(tit[mask_1 & mask_2])
print(tit.loc[mask_1 & mask_2, ['survived','sex','age']])

#survived   sex   age
#0           0  male  22.0
#1           1  male  38.0
#2           1  male  26.0
#3           1  male  35.0
#4           0  male  35.0
#6           0  male  54.0
#8           1  male  27.0
#11          1  male  58.0
#12          0  male  20.0
#13          0  male  39.0
#15          1  male  55.0
#18          0  male  31.0
#20          0  male  35.0

print(tit.loc[mask_1 | mask_2, ['survived','sex','age']])

mask_1 = tit.age.isin([17,18])
print(tit.loc[mask_1])

#survived  pclass   sex   age  sibsp  parch      fare embarked deck
#38          0       3  male  18.0      2      0   18.0000        S  NaN
#49          0       3  male  18.0      1      0   17.8000        S  NaN
#68          1       3  male  17.0      4      2    7.9250        S  NaN
#84          1       2  male  17.0      0      0   10.5000        S  NaN
#114         0       3  male  17.0      0      0   14.4583        C  NaN
#144         0       2  male  18.0      0      0   11.5000        S  NaN
#163         0       3  male  17.0      0      0    8.6625        S  NaN

mask_3 = tit.age.between(5,18, inclusive=True)
print(tit.loc[mask_3])
#survived  pclass   sex   age  sibsp  parch      fare embarked deck
#9           1       2  male  14.0      1      0   30.0708        C  NaN
#14          0       3  male  14.0      0      0    7.8542        S  NaN
#22          1       3  male  15.0      0      0    8.0292        Q  NaN
#24          0       3  male   8.0      3      1   21.0750        S  NaN
#38          0       3  male  18.0      2      0   18.0000        S  NaN


# une condition #Hay alguno?
condition = (tit.age==80.0).any()
print(condition)
#True

condition = (tit.age != 80.0).any()
print(condition)
#True

#ORiginal data again
tit = pd.read_csv("titanic.csv")
print(tit.head(3))

# une condition
condition1 = (tit.sex=='male').all()
print(condition1)
#False

# une autre condition
condition2 = (tit.sex=='female').all()
print(condition2)
#False

#HERARCHIE

import pandas as pd
import numpy as np
index = [['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,1,2]] # level 2 index
ser = pd.Series(np.random.randn(10), index = index)
print(ser)

#a  1    0.420487
#   2    0.839749
#   3   -1.286185
#b  1   -0.198529
#   2   -0.168503
#   3   -0.534460
#c  1    0.900748
#   2   -1.534282
#d  1    1.309346
#   2   -0.299453
#dtype: float64

print(ser['a'])

#1    0.420487
#2    0.839749
#3   -1.286185
#dtype: float64

print(ser['a'][2])
#0.8397486876338476

#Combiner et Fusionner les données : merge() & concat() Slider 43
#-----------------------------------------------------------------
import pandas as pd
df1 = pd.DataFrame({'key': ['a', 'b', 'c', 'd', 'e'],'A1': range(5), 'B1':range(5,10)})
df2 = pd.DataFrame({'key': ['a', 'b', 'c'], 'A2': range(3), 'B2':range(3,6)})
print(df1)
print(df2)

#Out[9]:
#    A1  B1 key
#0   0   5   a
#1   1   6   b
#2   2   7   c
#3   3   8   d
#4   4   9   e

#    A2  B2 key
#0   0   3   a
#1   1   4   b
#2   2   5   c

print(pd.merge(df1, df2, how = 'inner', on='key')) #inner cest intersection (abc) inner(interserction), outer(all), left, right

#    A1  B1 key  A2  B2
#0   0   5   a   0   3
#1   1   6   b   1   4
#2   2   7   c   2   5

print(pd.merge(df1, df2, how = 'outer', on='key'))  #regard inner ou outer relie  a la cle

#    A1  B1 key   A2   B2
#0   0   5   a  0.0  3.0
#1   1   6   b  1.0  4.0
#2   2   7   c  2.0  5.0
#3   3   8   d  NaN  NaN
#4   4   9   e  NaN  NaN

#Agréger les données : Groupby
#-----------------------------

import pandas as pd
data2 = {'Store':['Walmart','Walmart','Costco','Costco','Target','Target'],
        'Customer':['Tim','Jermy','Mark','Denice','Ray','Sam'],
        'Sales':[150,200,550,90,430,120]}
df2 = pd.DataFrame(data2)

print("Choix 1:")
by_store = df2.groupby("Store") #First Aggregate
by_store.mean() #Then user la function de groupement
#Sales
#Store
#Costco     320
#Target     275
#Walmart    175

by_store.min()

#          Customer  Sales
#Store
#Costco    Denice     90
#Target       Ray    120
#Walmart    Jermy    150


by_store.max()
by_store.std()
by_store.count()


by_store.describe()

by_store.describe().transpose()


by_store.describe().transpose()['Costco']

#Sales  count      2.000000
#        mean     320.000000
#        std      325.269119
#        min       90.000000
#        25%      205.000000
#        50%      320.000000
#        75%      435.000000
#        max      550.000000

#AI & Données | Pandas | unique() & nunique()
#---------------------------------------------

import numpy as np
import pandas as pd
data_dic = {'col_1':[1,2,3,4,5],
            'col_2':[111,222,333,111,555],
            'col_3':['alpha','bravo','charlie',np.nan,np.nan],
            }
df = pd.DataFrame(data_dic,index=[1,2,3,4,5])
df

print(df['col_1'].unique())
#[1 2 3 4 5]
print(df['col_2'].unique())
#[111 222 333 555]
print(df['col_3'].unique())  #Valores unicos
#['alpha' 'bravo' 'charlie' nan]

print(df['col_1'].nunique())
#5
print(df['col_2'].nunique())
#4
print(df['col_3'].nunique())  #numero de valores unicos
#3

#Expression lambda
#-----------------

import numpy as np
import pandas as pd
data_dic = {'col_1':[1,2,3,4,5],
            'col_2':[111,222,333,111,555],
            'col_3':['alpha','bravo','charlie',np.nan,np.nan],
            }
df = pd.DataFrame(data_dic,index=[1,2,3,4,5])

def square(value):
    return value*2

#Choix 1:
df['col_1'].apply(square)

#Choix 2:
df['col_1'].apply(lambda value:value*2)
#Out[14]:
#1     2
#2     4
#3     6
#4     8
#5    10

