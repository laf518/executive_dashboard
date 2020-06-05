# dash.py
import os
import pandas as pd


# User select which file to load:
file_path = os.path.join(os.path.dirname(__file__), "data")
f = os.listdir(file_path)

file_names = pd.Series(f)
file_name_data = pd.DataFrame(file_names, columns=['Files'])
    
print()
print("Available Reports:")
print("-----------------")
print(file_name_data)
print()
load_file = int(input("Please select the file number from the list above to generate a report: "))
selected_file = file_name_data.iloc[load_file, 0]

# STARTER CODE

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")