
import json

with open('first-letters-root.ser', encoding="utf8") as f:
    w = f.read()
    
y = w.split('i:')[1:]
d = {}

for k,i in enumerate(y):
    j = i.split(';')[1].split(':')
    # d[str(k)] = j[-1] # number as key
    d[j[-1]] = k # symbol as key

with open('first-letters-root.json', 'w') as f:
    json.dump(d, f)

info = open('first-letters-root.json')
res = json.load(info)
print(res)
