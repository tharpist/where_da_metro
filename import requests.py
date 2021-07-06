import requests

api_key='c8fcd95f3be44fd0a72731f248a35580'
url = 'https://api.wmata.com/TrainPositions/TrainPositions?contentType
header = {'api-key': api_key}
r =requests.get(url, headers=api_key)


print(r)