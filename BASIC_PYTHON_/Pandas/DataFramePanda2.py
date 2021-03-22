import numpy as np
import pandas as pd

#DataFrames
index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
array_2d = np.arange(0,100).reshape(10,10)
print(index)
print(columns)
print(array_2d)

df = pd.DataFrame(data = array_2d, index = index, columns = columns)
print(df.to_string())

#['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']
#['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10']
#[[ 0  1  2  3  4  5  6  7  8  9]
# [10 11 12 13 14 15 16 17 18 19]
#[20 21 22 23 24 25 26 27 28 29]
#[30 31 32 33 34 35 36 37 38 39]
#[40 41 42 43 44 45 46 47 48 49]
#[50 51 52 53 54 55 56 57 58 59]
#[60 61 62 63 64 65 66 67 68 69]
#[70 71 72 73 74 75 76 77 78 79]
#[80 81 82 83 84 85 86 87 88 89]
#[90 91 92 93 94 95 96 97 98 99]]


print(df['c1'])

#r1      0
#r2     10
#r3     20
#r4     30
#r5     40
#r6     50
#r7     60
#r8     70
#r9     80
#r10    90


print(type(df['c1']))
#Name: c1, dtype: int32

print(df.c1)
#r1      0
#r2     10
#r3     20
#r4     30
#r5     40
#r6     50
#r7     60
#r8     70
#r9     80
#r10    90

print(df[['c1', 'c10']])
#     c1  c10
#r1    0    9
#r2   10   19
#r3   20   29
#r4   30   39
#r5   40   49
#r6   50   59
#r7   60   69
#r8   70   79
#r9   80   89
#r10  90   99

df['new'] = df['c1'] + df['c2']
print(df['new'])
#r1       1
#r2      21
#r3      41
#r4      61
#r5      81
#r6     101
#r7     121
#r8     141
#r9     161
#r10    181

#Effacer coolonne
print(df.to_string())

#c1  c2  c3  c4  c5  c6  c7  c8  c9  c10  new
#r1    0   1   2   3   4   5   6   7   8    9    1
#r2   10  11  12  13  14  15  16  17  18   19   21
#r3   20  21  22  23  24  25  26  27  28   29   41
#r4   30  31  32  33  34  35  36  37  38   39   61
#r5   40  41  42  43  44  45  46  47  48   49   81
#r6   50  51  52  53  54  55  56  57  58   59  101
#r7   60  61  62  63  64  65  66  67  68   69  121
#r8   70  71  72  73  74  75  76  77  78   79  141
#r9   80  81  82  83  84  85  86  87  88   89  161
#r10  90  91  92  93  94  95  96  97  98   99  181

df.drop('new',axis = 1, inplace = False) #pas efface
print(df.to_string())

df.drop('new',axis = 1, inplace = True) #Efface cest comme confirmation

print(df.to_string())

#c1  c2  c3  c4  c5  c6  c7  c8  c9  c10
#r1    0   1   2   3   4   5   6   7   8    9
#r2   10  11  12  13  14  15  16  17  18   19
#r3   20  21  22  23  24  25  26  27  28   29
#r4   30  31  32  33  34  35  36  37  38   39
#r5   40  41  42  43  44  45  46  47  48   49
#r6   50  51  52  53  54  55  56  57  58   59
#r7   60  61  62  63  64  65  66  67  68   69
#r8   70  71  72  73  74  75  76  77  78   79
#r9   80  81  82  83  84  85  86  87  88   89
#r10  90  91  92  93  94  95  96  97  98   99

##TODO
#Que remarquez-vous?
#print(df['c1'] > 11)

#print(df[df['c1']>11])

#result = df[df['c1']>11]
#print(result['c1’])


#Operations avec masque booléen
#Exemple 2:
#import numpy as np
#import pandas as pd
#index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
#columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
#array_2d = np.arange(0,100).reshape(10,10)
#df = pd.DataFrame(data = array_2d, index = index, columns = columns)

#Que remarquez-vous?
#Choix 1:
#df[df['c1']>11][['c1','c9’]]
#                 vs

                 #Choix 2:
                #df[df['c1']>11].loc[['r3','r5']]


import numpy as np
import pandas as pd

index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
array_2d = np.arange(0,100).reshape(10,10)
df = pd.DataFrame(data = array_2d, index = index, columns = columns)

#Que remarquez-vous?
print(df[(df['c1']>60) & (df['c2']>80)])

#      c1  c2  c3  c4  c5  c6  c7  c8  c9  c10
#r9   80  81  82  83  84  85  86  87  88   89
#r10  90  91  92  93  94  95  96  97  98   99


#Choix 1:
print('choix 1')
print(df[df['c1']>80])
#choix 1
#c1  c2  c3  c4  c5  c6  c7  c8  c9  c10
#r10  90  91  92  93  94  95  96  97  98   99

print('choix 2')
result = df[df['c10']>80]
print(result['c10'])

#choix 2
#r9     89
#r10    99
#Name: c10, dtype: int32

print('choix 3')
print(df[df['c1']>11]['c1'])

#choix 3
#r3     20
#r4     30
#r5     40
#r6     50
#r7     60
#r8     70
#r9     80
#r10    90

#LOC TODO
#loc: ( location) accéder à un groupe de lignes ou colonnes par libellé(s)
#Exemple 1:
#import numpy as np
#import pandas as pd
#index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
#columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
#array_2d = np.arange(0,100).reshape(10,10)
#df = pd.DataFrame(data = array_2d, index = index, columns = columns)
#print(df.to_string())
#print(df.loc['r1’])

#Que remarquez-vous?
#print(df.loc['r1','r2’])?
#vs
#print(df.loc[['r1','r2’]]) ?



#              #Que remarquez-vous?
#              print(df.loc['c1’]) ?


# Que Remarquez-vous?
#print(df.loc['r1','c1’])

# Que Remarquez-vous?

#print(df.loc[['r1','r2'],['c1','c2’]])

    #                      print(df.loc[['r2','r5'],['c3','c4']])


#Change nom to columnas
import numpy as np
import pandas as pd
index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
array_2d = np.arange(0,100).reshape(10,10)
df = pd.DataFrame(data = array_2d, index = index, columns = columns)
print(df.to_string())

newind = 'a b c d e f g h i j'.split() # split at white spaces
df['newind']=newind
df.set_index('newind', inplace = True)

print(df.to_string())

#newind
#a        0   1   2   3   4   5   6   7   8    9
#b       10  11  12  13  14  15  16  17  18   19
#c       20  21  22  23  24  25  26  27  28   29
#d       30  31  32  33  34  35  36  37  38   39
#e       40  41  42  43  44  45  46  47  48   49
#f       50  51  52  53  54  55  56  57  58   59
#g       60  61  62  63  64  65  66  67  68   69
#h       70  71  72  73  74  75  76  77  78   79
#i       80  81  82  83  84  85  86  87  88   89
#j       90  91  92  93  94  95  96  97  98   99



df.reset_index(inplace = True) #index cest filas ientificatior.
print(df.to_string())

#newind  c1  c2  c3  c4  c5  c6  c7  c8  c9  c10
#0      a   0   1   2   3   4   5   6   7   8    9
#1      b  10  11  12  13  14  15  16  17  18   19
#2      c  20  21  22  23  24  25  26  27  28   29
#3      d  30  31  32  33  34  35  36  37  38   39
#4      e  40  41  42  43  44  45  46  47  48   49
#5      f  50  51  52  53  54  55  56  57  58   59
#6      g  60  61  62  63  64  65  66  67  68   69
#7      h  70  71  72  73  74  75  76  77  78   79
#8      i  80  81  82  83  84  85  86  87  88   89
#9      j  90  91  92  93  94  95  96  97  98   99

