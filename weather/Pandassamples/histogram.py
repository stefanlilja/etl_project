import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_json("tips.json")

# hostogram of total_bills
plt.hist(data['total_bill'])

plt.title("Histogram")

# Adding the legends
plt.show()

