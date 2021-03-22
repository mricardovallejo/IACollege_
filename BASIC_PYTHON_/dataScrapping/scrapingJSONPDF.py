
# Exemple: ok DOC  -  Il faut installer JAVA
import tika
from tika import parser
afile = 'C:\wrkOrion3\IACollege\BasicPhyton\dataScrapping\Analyste d’affaires.docx'
tika.initVM()
##contenu html
raw_xml = parser.from_file(afile, xmlContent=True)
text=raw_xml['content']
## contenu text
raw = parser.from_file(afile)
text=raw['content']
print(text)


# Exemple 2: PDF
afile = 'C:\wrkOrion3\IACollege\BasicPhyton\dataScrapping\Java Developer.pdf'
tika.initVM()
##contenu html
raw_xml = parser.from_file(afile, xmlContent=True)
text=raw_xml['content']
## contenu text
raw = parser.from_file(afile)
text=raw['content'] #Could be option metadata
print(text)