import pandas as pd
import matplotlib.pyplot as mpl

csv = pd.read_csv("pixelvault game sales.csv")

print("###################################\n")

# Task 1:
print("Task 1:\n")

print("###################################\n")
print(f"First five rows:\n\n{csv.head()}")
print(f"Last five rows:\n\n{csv.tail()}\n")

print("###################################\n")

print(f"Columns: {len(csv.columns)}")
print(f"Rows: {len(csv)}\n")

print("###################################\n")

# Task 2:
print("Task 2:\n")

print("###################################\n")
print(f"All Column names:\n\n{csv.columns.values}\n")
print("###################################\n")
print(f"Data types of all Columns:\n")
print(f"{csv.info()}\n")

print("###################################\n")

# Task 3:
print("Task 3:\n")

print("###################################\n")
print(f"Missing values in csv:\n{csv.isnull()}\n")
print("###################################\n")
print(f"Duplicate values in csv:\n{csv.duplicated()}\n")
print("###################################\n")

price = csv["price"]
quantity = csv["quantity"]

real_total_sale = price * quantity
print(f"Total sales per row:\n\n{real_total_sale}")

# Task 4:
print("Task 4:\n")

print("###################################\n")
print(f"Frequency of all games:\n\n{csv["game_title"].value_counts()}\n")
print(f"Highest frequency game:\n\n{csv["game_title"].mode()}\n")
print("###################################\n")

print(f"Frequency of all categories:\n\n{csv["category"].value_counts()}\n")
print(f"Highest number sales:\n\n{csv["category"].mode()}\n")
print("###################################\n")
print(f"Highest single total sale value:\n\n{csv["total_sale"].max()}\n")
print("###################################\n")
print(f"Average price of games sold:\n\n{csv.groupby("game_title", as_index=False)["price"].mean()}\n")