import os
import pandas as pd
import json


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))

def cleanse_data(filename):
    df = pd.read_json(parent_dir_path + f"\\data\\weather\\harmonized\\{filename}.json", orient='records')
    df.drop(
        columns=[
            'data_instant_details_air_pressure_at_sea_level',
            'data_instant_details_wind_from_direction',
            'data_next_12_hours_summary_symbol_code',
            'data_next_6_hours_summary_symbol_code',
            'data_next_6_hours_details_precipitation_amount'
        ], 
        inplace=True)
    df.rename(
        columns={
            'time': 'datetime',
            'data_instant_details_air_temperature': 'temperature',
            'data_instant_details_cloud_area_fraction': 'cloud_area_fraction',
            'data_instant_details_relative_humidity': 'humidity',
            'data_instant_details_wind_speed': 'wind_speed',
            'data_next_1_hours_summary_symbol_code': 'weather_description',
            'data_next_1_hours_details_precipitation_amount': 'precipitation'
        },
        inplace=True
    )
    # df = df.iloc[:62] 
    # rows 63 and onwards have no values for weather descripition and precipitation

    #print(df.to_string())

    df.to_json(parent_dir_path + f"\\data\\weather\\cleansed\\{filename}.json", orient='records')

