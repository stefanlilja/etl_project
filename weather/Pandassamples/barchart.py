import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_json("tips.json")

# Bar chart with day against tip
plt.bar(data['day'], data['tip'])

plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Adding the legends
plt.show()

