# dash.py
import os
import datetime
import pandas as pd
import numpy as np
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
    load_file = int(input("Please select the file number from the list above to generate a report: "))
    if load_file in list(file_name_data.index.values):
        selected_file = file_name_data.iloc[load_file, 0]
        break
    else:
        print("Invalid file number!")

selected_file = os.path.join(os.path.dirname(__file__), "data", selected_file)

# STARTER CODE

# Create dataframe from selected .csv file
data = pd.read_csv(selected_file)
df = pd.DataFrame(data)

# Create variables for required metrics
monthly_sales = df['sales price'].sum()

grouped_df = df.groupby('product').sum()
grouped_df = grouped_df.iloc[:, 2:]
grouped_df = grouped_df.sort_values(by='sales price', ascending=False)
grouped_df = grouped_df.head(5)
# breakpoint()

# Create variable for automated date display
x = f[load_file]
year = int(x[6:10])
month = int(x[10:12])
x  = datetime.datetime(year, month, 1)

print("-----------------------")
print("MONTH: ", x.strftime("%B"), x.strftime("%Y"))

print("-----------------------")
print("CRUNCHING THE DATA...")

# Monthly sales block
print("-----------------------")
print(f"TOTAL MONTHLY SALES: ${monthly_sales: .2f}")

# Monthly top-sales block
print("-----------------------")
print("TOP SELLING PRODUCTS:")
n = 1
while n <=5:
    print(f" {n: .0f}) ", grouped_df.index[n-1], f": ${grouped_df.iat[n-1, 0]: .2f}")
    n = n+1

# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")
breakpoint()

fig, ax = plt.subplots()

categories = list(grouped_df.index)
y_pos = np.arange(len(categories))
sales = list(round(grouped_df['sales price'], 2))

rect = ax.barh(y_pos, sales, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.invert_yaxis()
ax.set_xlabel('Sales')
ax.set_title('Monthly Sales by Category')

# def autolabel(rects):
#     for rec in rects:
#         width = rec.get_width()
#         ax.annotate(rec.get_x(),
#             xy=(width, rec.get_x() + rec.get_width() / 2),
#             xytext=(3, 0),
#             textcoords="offset points",
#             ha='center', va='bottom')

# autolabel(rect)

plt.show()