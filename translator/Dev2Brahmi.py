
from bs4 import BeautifulSoup as bs
import Devanagari as Dev
import requests
import json

link = 'https://imvickykumar999.github.io/Civilisation-Script-Translator/'
req = requests.get(link)

soup = bs(req.content, 'html5lib')
box = soup.findAll('table', attrs = {'class':"wikitable"})

tr = box[1].findAll('tr')
d={}

for i,j,k in zip(tr[0], tr[1], tr[2]):
    d[k.text.strip()] = [i.text.strip().replace('-',''), j.text.strip()] # symbol as key
    # d[i.text.strip().replace('-','')] = [k.text.strip(), j.text.strip()] # english as key

try:
    del(d['Devanagari'])
    del(d[''])
except:
    pass

# print(d) # hindi : [english, brahmi]
# c = Dev.devRange(6621, 6661)

c = Dev.devList(d.keys())
# print(c)

for i,j,k in zip(tr[0], tr[1], tr[2]):
    try:
        d[k.text.strip()] = [i.text.strip().replace('-',''), j.text.strip(), c[k.text.strip()]] # symbol as key
        # d[i.text.strip().replace('-','')] = [k.text.strip(), j.text.strip()] # english as key
    except:
        pass

print(d) # hindi : [english, brahmi, ser_code]
# print(len(d))

'''
-------------------------
Output:

{'क': ['k', '𑀓', 6621], 'ख': ['kh', '𑀔', 6622], 'ग': ['g', '𑀕', 6623], 'घ': ['gh', '𑀖', 6625], 'ङ': ['ṅ', '𑀗', 6626], 'च': ['c', '𑀘', 6627], 'छ': ['ch
', '𑀙', 6628], 'ज': ['j', '𑀚', 6629], 'झ': ['jh', '𑀛', 6632], 'ञ': ['ñ', '𑀜', 6633], 'ट': ['ṭ', '𑀝', 6634], 'ठ': ['ṭh', '𑀞', 6635], 'ड': ['ḍ', '𑀟', 6
636], 'ढ': ['ḍh', '𑀠', 6638], 'ण': ['ṇ', '𑀡', 6639], 'त': ['t', '𑀢', 6640], 'थ': ['th', '𑀣', 6641], 'द': ['d', '𑀤', 6642], 'ध': ['dh', '𑀥', 6643], 'न'
: ['n', '𑀦', 6644], 'प': ['p', '𑀧', 6645], 'फ': ['ph', '𑀨', 6646], 'ब': ['b', '𑀩', 6647], 'भ': ['bh', '𑀪', 6649], 'म': ['m', '𑀫', 6650], 'य': ['y', '�
'', 6651], 'र': ['r', '𑀭', 6653], 'ल': ['l', '𑀮', 6654], 'व': ['v', '𑀯', 6656], 'श': ['ś', '𑀰', 6657], 'ष': ['ṣ', '𑀱', 6658], 'स': ['s', '𑀲', 6659], '
ह': ['h', '𑀳', 6660]}
'''