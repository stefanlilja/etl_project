import requests
import json
import os


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))

def request_from_url(url):
    r = requests.get(url, headers={'User-Agent': 'TheSebastians'})
    return r.json()

def write_to_file(dict, filename):    
    with open(parent_dir_path + f'/data/weather/raw/{filename}.json', 'w') as file:
        json.dump(dict, file)


# test_url = 'http://swapi.dev/api/planets/1/'

# cape_town_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=-34&lon=18'

# json_data = request_from_url(cape_town_url)

# write_to_file(json_data)
