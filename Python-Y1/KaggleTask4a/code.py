import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("amazon_sales_dataset.csv")

## Task 1.1
print(f"First five rows: {file.head()}")

## Task 1.2
print(f"Number of Columns: {len(file.columns.values)}\nNumber of Rows: {len(file)}\nName of Columns: {file.columns.values}")

## Task 2.1
total_sales = file["quantity_sold"].sum()
sales_value = file["price"].sum() / len(file)
print(f"Total Sales: {total_sales} sales\nAverage Sales Value: £{round(sales_value, 2)}")

## Task 3.1
category = file.groupby("product_category")["quantity_sold"].sum()

plt.figure(figsize=(12, 8))
plt.bar(category.index, category.values)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## Task 4.1
region = file.groupby("customer_region")["quantity_sold"].sum()

plt.figure(figsize=(12, 8))
plt.bar(region.index, region.values)
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()