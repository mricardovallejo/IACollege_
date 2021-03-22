import numpy as np

#Create series
import pandas as pd
my_data = [100,200,300]
c=pd.Series(data = my_data)
print(c)

#Create series with labels
import numpy as np
import pandas as pd
my_labels = ['x','y','z']
my_data = [100,200,300]
c=pd.Series(data = my_data, index = my_labels)
print(c)

#SErie a apratir d array
import numpy as np
import pandas as pd
my_data = [100,200,300]
my_array = np.array(my_data)
pd.Series(data = my_array)

import numpy as np
import pandas as pd
my_labels = ['x','y','z']
my_data = [100,200,300]
my_array = np.array(my_data)
pd.Series(data = my_array, index = my_labels)

#Serie a partir de dictionaire
my_dic = {'m':100,'m':200,'p':300}
k = pd.Series(my_dic)
print(k)  #Take the las m:200 ATTENTION!!

my_labels = ['x','y','z']
k = pd.Series(data = my_labels)
print(k)

# Dictionaire with cle alphabetic

dic_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dic_2 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dic_3 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700, 'Jasper':1000}
ser1 = pd.Series(dic_1)
ser2 = pd.Series(dic_2)
ser3 = pd.Series(dic_3)

# que remarquez-vous?
print(ser1)
print(ser2)

print(ser1['Calgary'])  #print 200

#sum keys onlys sum avec le meme cle
ser4 = ser1 + ser2
ser5 = ser2 + ser3
print(ser4)
print(ser5)
print(ser4.isnull())
print(ser5.notnull())


#Info de la serie
dic_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
ser1 = pd.Series(dic_1)
print(ser1.axes)
print(ser1.values)

dic_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
ser1 = pd.Series(dic_1)
print(ser1.head(1)) # renvoie le(s) première(s) ligne(s)
print(ser1.tail(1)) #renvoie le(s) dernière(s) colonne(s)

dic_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
ser1 = pd.Series(dic_1)
print(ser1.size)

dic_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
ser1 = pd.Series(dic_1)
print(ser1.empty)


