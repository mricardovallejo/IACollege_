from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

# Methode 1 - ok
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# Methode 2 - ok
import requests as requests
x = requests.get(url)
print(x.text)

# Methode 3 -
from bs4 import BeautifulSoup

res= requests.get('https://news.ycombinator.com/newest')
print(res)
txt_html=BeautifulSoup(res.text,'html.parser')
print(txt_html)

# Recuperation de donnes

## select : css selectors
#https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
#https://docs.python.org/3/library/pprint.html


import pprint
import json

histoires=txt_html.select('.storylink')  #cest la class css
votes=txt_html.select('.score')

hist=[]
for i, item in enumerate(histoires):
   titre = histoires[i].getText()
   href = histoires[i].get('href',None)
   vote = votes[i].getText()
   hist.append({'titre': titre, 'link':href, 'votes':vote})

#Print JSON
print(json.dumps(hist, indent=4, sort_keys=True))

#print

### Excercise 2 -  REDDIT

res= requests.get('https://www.reddit.com/r/news/')
txt_html2 = BeautifulSoup(res.text, 'html.parser')
print(txt_html2)

#newstittre = txt_html2.find_all("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
newstittre = txt_html2.find_all('h3')

hist2 = []
for i, item in enumerate(newstittre):
    titre = newstittre[i].getText()
    hist2.append({'titre': titre})

print(json.dumps(hist2, indent=1, sort_keys=True))