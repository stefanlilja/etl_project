import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 
import plotly.graph_objects as go
from dash import Dash, Input, Output, html, dcc, ctx



conn = psycopg2.connect(
    host="localhost",
    database="etl_mini_project",
    user="postgres",
    password="continuousimpliesintegrable")
    

cur = conn.cursor()

# Execute a SELECT statement to retrieve data
cur.execute("SELECT * FROM forecast;")

# Fetch all rows
data = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

df = pd.DataFrame(data, columns=[desc[0] for desc in cur.description])

df = df[df['current_datetime']=='2023-01-20 13:21:29.46907']


app = Dash()

app.layout = html.Div(
    [
        dcc.Graph(id='graph_plotly'),
        dcc.RadioItems(
            id='radioitems', 
            options=[
                {'label': 'Temperature (°C)', 'value': 'temperature'},
                {'label': 'Wind speed (m/s)', 'value': 'wind_speed'},
                {'label': 'Humidity (%)', 'value': 'humidity'},
                {'label': 'Cloudiness (%)', 'value': 'cloud_area_fraction'},
                {'label': 'Precipitation (mm)', 'value': 'precipitation'}
                ], 
            value='temperature',
            labelStyle={'display': 'block'}
        )        
    ]
)

@app.callback(
    Output(component_id = 'graph_plotly', component_property = 'figure'),
    [Input(component_id = 'radioitems', component_property = 'value')]
)
def graph_update(radio_values):
    figure = px.line(df, x = "forecast_datetime", y = radio_values, markers = True, color = "location_id")

    figure.update_layout(
    font_family = "Arial",
    font_color = "#000000",
    font_size = 20,
    legend_title = "Countries",
    title_font_family = "Verdana",
    title_font_size = 30,
    title_font_color = "#ACACAC",
    yaxis_title = "Value",
    xaxis_title = "Timeline",
    title = "Forecast",
    showlegend=True,
    )
    figure.data[0].name='Svalbard'
    figure.data[1].name='Åkersberga'
    figure.data[2].name='Vatican city'
    figure.data[3].name="N'Djamena"
    figure.data[4].name='Kinshasa'
    figure.data[5].name='Cape town'
    figure.data[6].name='Princess Elizabeth station'

    return figure

app.run_server(debug=True, use_reloader=True)