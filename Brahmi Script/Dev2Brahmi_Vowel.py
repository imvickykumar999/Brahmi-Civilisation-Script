
import pandas as pd
import json

url = 'https://imvickykumar999.github.io/Civilisation-Script-Translator/'
table = pd.read_html(url)[2].T.fillna(" ")

lst = table.to_dict('dict')
# lst = table.to_dict('list')
# lst = table.to_dict('series')
# lst = table.to_dict('split')
# lst = table.to_dict('records')
# lst = table.to_dict('index')

# print(lst)

with open('data_files/vowel.json', 'w') as fp:
    json.dump(lst, fp)

with open("data_files/vowel.json", "r") as json_file:
    my_dict = json.load(json_file)

for i in my_dict:
    print(i, my_dict[i])
    print()

# -----------------------------------------------------------

# from bs4 import BeautifulSoup as bs
# import requests
# import csv

# req = requests.get(url)
# file = req.content

# file = open('data_files/vowel_table.html', 'r', encoding='utf-8')
# soup = bs(file, 'html5lib')

# box = soup.findAll('table', attrs = {'class':"wikitable"})
# # print(box)

# tr = box[0].findAll('tr')
# lst=[]

# for i in tr:
#     head = i.text.strip().replace('-','').replace('\n',',').split(',')
#     lst.append(head)

# try:
#     with open('data_files/vowel.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(lst)
# except Exception as e:
#     print(e)
