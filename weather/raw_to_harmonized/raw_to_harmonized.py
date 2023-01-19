import os
import pandas as pd
import json


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))


def read_raw_data(filename):    
    with open(parent_dir_path + f'\\data\\weather\\raw\\{filename}.json', 'r') as file:
        raw_text = file.readline()

    raw_data = json.loads(raw_text)

    timeseries = raw_data['properties']['timeseries']
    df = pd.json_normalize(timeseries, sep='_')
    return df



def write_to_harmonized(df, filename):
    filepath = parent_dir_path + f'\\data\\weather\\harmonized\\{filename}.json'
    df.to_json(filepath, orient='records')
    

