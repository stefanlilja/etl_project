import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 



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


figure = px.line(df, x = "forecast_datetime", y = "temperature", color = "location_id")

figure.update_layout(
font_family = "Arial",
font_color = "#000000",
font_size = 20,
legend_title = "Countries",
title_font_family = "Verdana",
title_font_size = 30,
title_font_color = "#ACACAC",
#legend_title_font_color = "green" # 
yaxis_title = "Temperature",
title = "Forecast",
showlegend=True,
)
figure.show()






