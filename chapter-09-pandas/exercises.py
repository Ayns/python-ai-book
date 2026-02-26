# Chapter 9 - Exercise Solutions
import pandas as pd

# 1. Create sample data and analyze
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
    "Region": ["North", "North", "South", "South", "North", "South"],
    "Sales": [1200, 800, 600, 1100, 900, 550],
    "Units": [10, 25, 15, 8, 30, 12],
}
df = pd.DataFrame(data)

# Group by product and calculate totals
print(df.groupby("Product")["Sales"].agg(["sum", "mean", "count"]))

# 2. Filter and sort
top_sales = df[df["Sales"] > 700].sort_values("Sales", ascending=False)
print("\nSales > $700:")
print(top_sales)

# 3. Add calculated column
df["Revenue_Per_Unit"] = df["Sales"] / df["Units"]
print("\nWith Revenue Per Unit:")
print(df)

# 4. Export results
df.to_csv("analysis_output.csv", index=False)
print("\nSaved to analysis_output.csv")
