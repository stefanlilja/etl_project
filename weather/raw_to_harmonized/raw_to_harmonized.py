import os
import pandas as pd
import json


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))


def read_raw_data():
    
    with open(parent_dir_path + '\\data\\weather\\raw\\data.json', 'r') as file:
        raw_text = file.readline()

    raw_data = json.loads(raw_text)

    timeseries = raw_data['properties']['timeseries']
    df = pd.json_normalize(timeseries, sep='_')
    return df


filepath = parent_dir_path + '\\data\\weather\\harmonized\\data.json'
def write_to_harmonized(df, filepath):
    # not used currently
    df.to_json(filepath, orient='records')
    

        
df = read_raw_data()
df.to_json(filepath, orient='records')
