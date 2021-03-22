import pandas as pd

#API
ipd =pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=10')

ipd[['state', 'title', 'updated_at']].head()

print(ipd)


#Excell

objet_excel=pd.read_excel("../data/credit.xlsx", sheetname="donnees")
dico_frame={}
for feuille in objet_excel.sheet_names :

    if feuille.find("_data")>0 :
        dico_frame[feuille]=objet_excel.parse(feuille)
