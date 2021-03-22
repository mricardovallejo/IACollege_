from pandas import Series
import numpy as np


obj = Series([4,7,-5,3])
print(obj.values)
print(obj.index)

#[ 4  7 -5  3]
#RangeIndex(start=0, stop=4, step=1)


obj2=Series([4,7,-5,3], index=['d','b','a','c'])
print(obj2)
#d    4
#b    7
#a   -5
#c    3

print(obj2.index)
#Index(['d', 'b', 'a', 'c'], dtype='object')

print(obj2['a'])
#-5
print(obj2['d'])
print(obj2[['c','a','d']])
#c    3
#a   -5
#d    4
print(obj2[obj2>0])
#d    4
#b    7
#c    3
print(obj2*2)
#d     8
#b    14
#a   -10
#c     6


print(np.exp(obj2))
#d      54.598150
#b    1096.633158
#a       0.006738

ma_serie1= Series(np.random.randn(5), index=["A","B","C","D","E"])
print(ma_serie1)
#A    0.887223
#B    0.014654
#C    0.418020
#D    0.709925
#E   -0.706396
#dtype: float64


ma_serie2 = Series([8,70,320, 1200], index=["Suisse","France","USA","Chine"])
print(ma_serie2)

#Suisse       8
#France      70
#USA        320
#Chine     1200
#dtype: int64


ma_serie3= Series({"Suisse" :8,"France" :70,"USA" :320,"Chine" :1200})
print(ma_serie3)

#Chine     1200
#France      70
#Suisse       8
#USA        320
#dtype: int64

ma_serie2 = Series([8,70,320, 1200], index=["Suisse","France","USA","Chine"])
print(ma_serie2[:3])

#Suisse 8
#France 70
#USA 320
#dtype : int64

print(ma_serie2[ma_serie>50])

#USA 250
#Chine 1200
#dtype : int64


print(ma_serie2[(ma_serie>500)|(ma_serie<50)])
#Out[] :
#Suisse 8
#Chine 1200
#dtype : int64

