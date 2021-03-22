import pandas as pd # This is always assumed but is included here as an introduction.
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 2, 1, 4, 3, 5, 2, 3, 4, 1],
                   'B': [12, 14, 11, 16, 18, 18, 22, 13, 21, 17],
                   'C': ['a', 'a', 'b', 'a', 'b', 'c', 'b', 'a', 'b', 'a']})

print(df)

#   A   B  C
#0  1  12  a
#1  2  14  a
#2  1  11  b
#3  4  16  a
#4  3  18  b
#5  5  18  c
#6  2  22  b
#7  3  13  a
#8  4  21  b
#9  1  17  a


df.describe()

#        A          B
#count  10.000000  10.000000
#mean    2.600000  16.200000
#std     1.429841   3.705851
#min     1.000000  11.000000
#25%     1.250000  13.250000
#50%     2.500000  16.500000
#75%     3.750000  18.000000
#max     5.000000  22.000000


df['C'].describe()

#count     10
#unique     3
#top        a
#freq       5
#Name: C, dtype: objec


#Creation sans data de un dataFrame
df = pd.DataFrame(columns = ['A', 'B', 'C'])

df.loc[0, 'A'] = 1  #loc usa como indices el INDEX(x) y el LABEL(y)
print(df)
#  A  B   C
#0 1 NaN NaN


#Pag 14