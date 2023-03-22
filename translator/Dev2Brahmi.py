
from bs4 import BeautifulSoup as bs, NavigableString, Tag
import requests

link = 'https://imvickykumar999.github.io/Civilisation-Script-Translator/'
req = requests.get(link)

soup = bs(req.content, 'html5lib')
# print(list(soup.body))
box = soup.findAll('table', attrs = {'class':"wikitable"})

# for body_child in soup.body.children:
#     if isinstance(body_child, NavigableString):
#         continue
#     if isinstance(body_child, Tag):
#         print(body_child.name)

tr = box[1].findAll('tr')
for i in tr[0]:
    print(i)
