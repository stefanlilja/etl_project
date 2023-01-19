import pandas as pd
import psycopg2
import os

def connectdb():
    conn = psycopg2.connect(
        host="localhost",
        database="etl_mini_project",
        user="postgres",
        password="sudden21")
    return conn

current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))
df = pd.read_json(parent_dir_path + "\\data\\weather\\cleansed\\data.json", orient='records')

column_names = "location_id, current_datetime, forecast_datetime, temperature, cloud_area_fraction,\
                humidity, wind_speed, weather_description, precipitation"

def insert(conn, location_id, current_datetime, df):
    conn = connectdb()
    cur = conn.cursor()
    for i in range(len(df)):
        row = df.iloc[i]
        cur.execute(f"INSERT INTO forecast ({column_names}) VALUES ('{location_id}', '{current_datetime}', '{row['datetime']}',\
                    {row['temperature']}, {row['cloud_area_fraction']}, {row['humidity']}, {row['wind_speed']},\
                    {replace_None_value(row['weather_description'])}, {replace_nan_value(row['precipitation'])})")
    conn.commit()
    cur.close()

def replace_None_value(value):
    if value == None:
        return "NULL"
    else:
        return f"'{value}'"

def replace_nan_value(value):
    if str(value) == 'nan':
        return "NULL"
    else:
        return value

current_datetime ='2023-01-19 12:00:00+00:00'
conn = connectdb()
cape_town_id = 6

insert(conn, cape_town_id, current_datetime, df)


# for i in range(len(df)):
#     row = df.iloc[i]
#     print(row['humidity'])


        # for i in range(len(hour_data_json["station"])):
        # if hour_data_json["station"][i]["value"] is not None:
        #     station_id = int(hour_data_json["station"][i]["key"])
        #     station_name = hour_data_json["station"][i]["name"]
        #     station_owner = hour_data_json["station"][i]["owner"]
        #     station_longitude = hour_data_json["station"][i]["longitude"]
        #     station_latitude = hour_data_json["station"][i]["latitude"]
        #     station_temperature = hour_data_json["station"][i]["value"][0]["value"]
        #     station_value_quality = hour_data_json["station"][i]["value"][0]["quality"]
        #     station_value_date = hour_data_json["station"][i]["value"][0]["date"]
        #     station_height = hour_data_json["station"][i]["height"]