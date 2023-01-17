import requests
import json
import os


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))

def request_from_url(url):
    r = requests.get(url)
    return r.json()

def write_to_file(dict):
    
    with open(parent_dir_path + '\\data\\testing\\raw\\data.json', 'w') as file:
        json.dump(dict, file)


test_url = 'http://swapi.dev/api/planets/1/'

json_data = request_from_url(test_url)

write_to_file(json_data)
