import pandas as pd
import matplotlib.pyplot as plt
import os


current_dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(current_dir_path, os.pardir))
# reading the database
data = pd.read_json(parent_dir_path + "\\data\\weather\\cleansed\\data.json", orient='records')

# Scatter plot with day against tip
plt.plot(data['datetime'], data['temperature'])



# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()

