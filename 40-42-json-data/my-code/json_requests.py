#!python3

import os
import json
import requests
from pprint import pprint

base_folder = os.path.dirname(__file__)
filename = os.path.join(base_folder, 'mount-data.json')

# https://stackoverflow.com/questions/37228114/opening-a-json-file-in-python
with open(filename, 'r', encoding='utf-8') as fin:
    #data = list(json.load(fin).items())
    # data = json.load(fin).items() # not subscriptable !? 
    data = json.load(fin) 

# for item in data.items():
 #    pprint(item)

pprint(type(data))
print()
# print(data[0]) # results in <class 'list'> and ('achievementPoints', 14565) if using data = list(json.load(fin).items())

print(data['class'])


# for item in data['mounts']:
#     pprint(item)
    
# for item in data['mounts']['collected']:
#     pprint(item)
    
for item in data['mounts']['collected']:
    pprint(item['name'])
    
is_flying = []
for mount in data['mounts']['collected']:
    if mount['isFlying']:
        is_flying.append(mount)

#Collects all of the applicable mounts and stores them as a list of dicts

#You can then work with the data as normal:

print(len(is_flying))

for i in is_flying:
    print(i)

for i in is_flying:
    print(i['name'])

