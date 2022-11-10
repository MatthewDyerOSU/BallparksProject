import requests
import json

search_term = "angel stadium"

search_url = 'http://localhost:8080/{}'.format(search_term)

try:
    response = requests.get(search_url)
    response_dny = json.loads(response.text)
    history = response_dny['history']
    print(history)
except:
    print('unable to retreive stadium history')