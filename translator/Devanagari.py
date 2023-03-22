
# https://www.fileformat.info/info/unicode/block/devanagari/index.htm

import json

info = open('first-letters-root/first-letters-root.json')
res = json.load(info)

for i in range(6595, 6661):
    print(i, res[str(i)])
