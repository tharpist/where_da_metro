import requests
import json
import pprint

from requests import api
from config import config

#url = 'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/A09'
#url = 'https://api.wmata.com/TrainPositions/TrainPositions?contentType=json HTTP/1.1'

def get_station(station):
    station_url = config['url'] + station
    config['url'] = station_url
    data = config
    return data


def fetch_data(data):
    r = requests.get(url=data['url'],
    headers = data
        )
    train_data = r.json()
    return train_data

def send_message(train_data):    
    message = []
    for k, trains in train_data.items():
        for train in trains:
            #hardcoded can i get this automated in case if htere is ever a new line?
            line = train['Line']
            if line == 'RD':
                line = 'Red'
            if line == 'BL':
                line = 'Blue'
            if line == 'YL':
                line = 'Yellow'
            if line == 'OR':
                line == 'Orange'
            if line == 'GR':
                line = 'Green'
            if line == 'SV':
                line = 'Silver'

            
            destination = train['Destination']
            arrival = train['Min']
            if arrival == 'ARR':
                message.append(f"{line} line train  heading to {destination} is arriving now!")
            message.append(f"{line} line train heading to {destination} will be arriving in {arrival} minutes")
    return message



#stationz = get_station('a09')
#fetch_data(stationz)
