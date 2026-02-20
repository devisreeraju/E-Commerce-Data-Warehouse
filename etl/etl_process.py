import pandas as pd

# Load datasets
orders = pd.read_csv("data/List of Orders.csv")
details = pd.read_csv("data/Order Details.csv")
targets = pd.read_csv("data/Sales target.csv")

print("Orders Data:")
print(orders.head())

print("\nOrder Details Data:")
print(details.head())

print("\nSales Target Data:")
print(targets.head())
# Merge Orders and Order Details
merged_data = pd.merge(orders, details, on="Order ID")

print("\nMerged Data:")
print(merged_data.head())
# Create Revenue column
merged_data["Revenue"] = merged_data["Amount"] * merged_data["Quantity"]

print("\nWith Revenue:")
print(merged_data.head())
# Save processed file
merged_data.to_csv("data/processed_sales.csv", index=False)

print("\nProcessed file saved successfully!")
# Convert Order Date to datetime
merged_data["Order Date"] = pd.to_datetime(merged_data["Order Date"], dayfirst=True)

# Extract Month and Year
merged_data["Month"] = merged_data["Order Date"].dt.month
merged_data["Year"] = merged_data["Order Date"].dt.year

import sqlite3

# Create connection
conn = sqlite3.connect("ecommerce.db")

# Load processed data into database
merged_data.to_sql("sales_data", conn, if_exists="replace", index=False)

print("\nData loaded into SQLite database successfully!")

conn.close()
