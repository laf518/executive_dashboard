# dash.py
import os
import datetime
import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# User selects which file to load:
file_path = os.path.join(os.path.dirname(__file__), "data")
f = os.listdir(file_path)

file_names = pd.Series(f)
file_name_data = pd.DataFrame(file_names, columns=['Files'])

print()
print("Available Reports:")
print("-----------------")
print(file_name_data)
print()

# Validate user input:
while True:
    try:
        load_file = int(input("Please select the file number from the list above to generate a report: "))
        if load_file in list(file_name_data.index.values):
            selected_file = file_name_data.iloc[load_file, 0]
            break
        else:
            print("Invalid file number!")
    except ValueError:
        print("Input was not a number. Please try again...")

selected_file = os.path.join(os.path.dirname(__file__), "data", selected_file)

# Create dataframe from selected .csv file
data = pd.read_csv(selected_file)
df = pd.DataFrame(data)

# Create variables for required metrics
monthly_sales = df['sales price'].sum()

grouped_df = df.groupby('product').sum()
grouped_df = grouped_df.iloc[:, 2:]
grouped_df = grouped_df.sort_values(by='sales price', ascending=False)
top_grouped_df = grouped_df.head(5)

# Create variable for automated date display
x = f[load_file]
year = int(x[6:10])
month = int(x[10:12])
x  = datetime.datetime(year, month, 1)

# Automated file display
print("-----------------------")
print("MONTH: ", x.strftime("%B"), x.strftime("%Y"))

print("-----------------------")
print("CRUNCHING THE DATA...")

# Monthly sales block
print("-----------------------")
print(f"TOTAL MONTHLY SALES: ${monthly_sales:,.2f}")

# Monthly top-sales block
print("-----------------------")
print("TOP SELLING PRODUCTS:")
n = 1
while n <=5:
    print(f" {n:.0f}) ", top_grouped_df.index[n-1], f": ${top_grouped_df.iat[n-1, 0]:,.2f}")
    n = n+1

# Visualization block
print("-----------------------")
print("VISUALIZING THE DATA...")

# Horizontal Bar Graph Set Up:
fig, ax = plt.subplots()

categories = list(grouped_df.index)
sales = list(round(grouped_df['sales price'], 2))
y_pos = np.arange(len(categories))
x_lab = [f"${x:,.2f}" for x in range(0, (round(math.ceil(sales[0] / 1000)) * 1000) + 1000, 1000)]

ax.barh(y_pos, sales, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xticklabels(x_lab)
ax.invert_yaxis()
ax.set_xlabel('Sales (USD)', fontweight = 'bold')
ax.set_ylabel('Category', fontweight = 'bold')
ax.set_title('Monthly Sales by Category', fontweight = 'bold')
# CREDIT: https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html
# CREDIT: https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barh.html

# Label each bar with exact sales figure:
for i, v in enumerate(sales):
    if v > 1000:
        val = f"${v:,.2f}"
        ax.text(v - 600, i + .1, val, color = 'white', fontweight = 'bold')
    else:
        val = f"${v:,.2f}"
        ax.text(v + 3, i + .1, val, color = 'blue', fontweight = 'bold')
# CREDIT: https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
plt.show()