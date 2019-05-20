import json
import requests
from pprint import pprint

FILM_INFO_REQ = input("Enter a film to get the OMBd score for it: ")
print(f"You entered: {FILM_INFO_REQ}\n")

# r = requests.get('http://www.omdbapi.com/?apikey=36c2ca2a&t=top gun')
# can't work!!! r = requests.get("http://www.omdbapi.com/?apikey=36c2ca2a&t='FILM_INFO_REQ'")
r = requests.get("http://www.omdbapi.com/?apikey=36c2ca2a&t=" + FILM_INFO_REQ)

data = json.loads(r.text)

pprint(data)

print()
pprint(['Title'])
print(f"The title of the film is {data['Title']}")
print()
print(data['Ratings'])
print()
print(data['Ratings'][1])
print()
print(data['Ratings'][1]['Source'])
print()
print(f"The {data['Ratings'][1]['Source']} score for {data['Title']} is {data['Ratings'][1]['Value']}")