import source_to_raw.source_to_raw as str
import raw_to_harmonized.raw_to_harmonized as rth
import harmonized_to_cleansed.harmonized_to_cleansed as htc
import sql_script.database_insertion as di

from datetime import datetime


cape_town_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=-34&lon=18'

location_names = ['Svalbard', 'Åkersberga', 'Vatican_city', "N_Djamena", 'Kinshasa', 'Cape_town', 'Princess_Elizabeth_station']
location_coordinates = [('78', '17'), ('59', '18'), ('42', '12'), ('12', '15'), ('-4', '15'), ('-34', '18'), ('-72', '23')]
time = datetime.now()

# Source to raw
def download_from_api():
    for name, coordinates in zip(location_names, location_coordinates):
        url = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={coordinates[0]}&lon={coordinates[1]}'
        data = str.request_from_url(url)
        filename = name + time.strftime('%Y_%m_%d')
        str.write_to_file(data, filename)

# def testing():
#     data_test = str.request_from_url(cape_town_url)
#     str.write_to_file(data_test, 'testing_data')

# Raw to harmonized
def raw_to_harm():
    for name in (location_names):
        filename = name + time.strftime('%Y_%m_%d')
        data = rth.read_raw_data(filename)
        rth.write_to_harmonized(data, filename)

if __name__ == '__main__':
    download_from_api()
    
