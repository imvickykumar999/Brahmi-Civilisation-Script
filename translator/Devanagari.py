
# https://www.fileformat.info/info/unicode/block/devanagari/index.htm

import json
info = open('first-letters-root/first-letters-root.json')
res = json.load(info)

def devRange(a = 6595, b = 6661, p=0):
    # print(len(res))
    c={}

    for i in range(a, b):
        c[i] = res[str(i)]
        if p:
            print(i, res[str(i)], end='\t')

    return c

def devList(key, p=0):
    # print(len(res))
    c={}

    for i in key:
        c[i] = res[f'"{i}"']
        if p:
            print(i, res[f'"{i}"'], end='\t')
    return c

# devRange(6621, 6661, 1)
