
from bs4 import BeautifulSoup as bs
from firstlettersroot import Devanagari as Dev
import requests, json
import pandas as pd

link = 'https://imvickykumar999.github.io/Civilisation-Script-Translator/'
req = requests.get(link)

soup = bs(req.content, 'html5lib')
box = soup.findAll('table', attrs = {'class':"wikitable"})

tr = box[1].findAll('tr')
d={}

for i,j,k in zip(tr[0], tr[1], tr[2]):
    d[k.text.strip()] = [i.text.strip().replace('-',''), 
                         j.text.strip()]

try:
    del(d['Devanagari'])
    del(d[''])
except:
    pass

# print(d) # hindi : [english, brahmi]
c = Dev.devList(d.keys())
# print(c)

for i,j,k in zip(tr[0], tr[1], tr[2]):
    try:
        d[k.text.strip()] = [i.text.strip().replace('-',''), 
                             j.text.strip(), c[k.text.strip()]]
    except:
        pass

# print(d) # hindi : [english, brahmi, ser_code]
# print(len(d))

with open('data_files/devanagari.json', 'w') as f:
    json.dump(d, f)

info = open('data_files/devanagari.json')
res = json.load(info)
# print(res)

d={}
print('English, Hindi, Brahmi, Ser_Code')
print('-'*32, end='\n\n')

for i in res:
    print(res[i][0], '\t', i, '\t', res[i][1], '\t', res[i][2])
    d.update({res[i][0] : [i, res[i][1], res[i][2]]})
# print(d)

df = pd.DataFrame.from_dict(data=d, orient='index')
# print(df)
df.to_csv('data_files/devanagari.csv', header=False)


'''
Output:

English, Hindi, Brahmi, Ser_Code
--------------------------------

k        क       𑀓       6621
kh       ख       𑀔       6622
g        ग       𑀕       6623
gh       घ       𑀖       6625
ṅ        ङ       𑀗       6626
c        च       𑀘       6627
ch       छ       𑀙       6628
j        ज       𑀚       6629
jh       झ       𑀛       6632
ñ        ञ       𑀜       6633
ṭ        ट       𑀝       6634
ṭh       ठ       𑀞       6635
ḍ        ड       𑀟       6636
ḍh       ढ       𑀠       6638
ṇ        ण       𑀡       6639
t        त       𑀢       6640
th       थ       𑀣       6641
d        द       𑀤       6642
dh       ध       𑀥       6643
n        न       𑀦       6644
p        प       𑀧       6645
ph       फ       𑀨       6646
b        ब       𑀩       6647
bh       भ       𑀪       6649
m        म       𑀫       6650
y        य       𑀬       6651
r        र       𑀭       6653
l        ल       𑀮       6654
v        व       𑀯       6656
ś        श       𑀰       6657
ṣ        ष       𑀱       6658
s        स       𑀲       6659
h        ह       𑀳       6660

'''