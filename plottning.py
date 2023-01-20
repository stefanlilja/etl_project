import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


conn = psycopg2.connect(
    host="localhost",
    database="etl_mini_project",
    user="postgres",
    password="sudden21")
    

cur = conn.cursor()

# Execute a SELECT statement to retrieve data
cur.execute("SELECT * FROM forecast")

# Fetch all rows
data = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

df = pd.DataFrame(data, columns=[desc[0] for desc in cur.description])
"""
plt.plot(df['forecast_datetime'], df['temperature'], label='Temperature')
plt.title("Weather Forecast")
plt.xlabel("Forecast DateTime")
plt.ylabel("Temperature")


# Create a bar plot of cloud_area_fraction and forecast_datetime
plt.bar(df['forecast_datetime'], df['cloud_area_fraction'], label='Cloud Area Fraction')
plt.title("Weather Forecast")
plt.xlabel("Forecast DateTime")
plt.ylabel("Values")

# Create a scatter plot of humidity and forecast_datetime
plt.scatter(df['forecast_datetime'], df['humidity'], label='Humidity')
plt.title("Weather Forecast")
plt.xlabel("Forecast DateTime")
plt.ylabel("Values")

# Create a line plot of wind_speed and forecast_datetime
plt.plot(df['forecast_datetime'], df['wind_speed'], label='Wind Speed')
plt.title("Weather Forecast")
plt.xlabel("Forecast DateTime")
plt.ylabel("Windspeed")
plt.show()
"""


# Create a bar plot of precipitation and forecast_datetime
plt.bar(df['forecast_datetime'], df['precipitation'], label='Precipitation')
plt.title("Weather Forecast")
plt.xlabel("Forecast DateTime")
plt.ylabel("Precipitation")
plt.show()


# Display the plot


