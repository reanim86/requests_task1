import requests
from pprint import pprint
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
superhero = response.json()
pprint(superhero)

