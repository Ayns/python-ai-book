# Sales Data Analyzer - Chapter 9 Project

import pandas as pd
import os


def create_sample_data():
    """Create sample sales data if no file exists"""
    data = {
        "Date": ["2026-01-05", "2026-01-12", "2026-01-20", "2026-02-03",
                 "2026-02-14", "2026-02-28", "2026-03-10", "2026-03-22"],
        "Product": ["Laptop", "Phone", "Tablet", "Laptop",
                    "Phone", "Headphones", "Laptop", "Tablet"],
        "Category": ["Electronics", "Electronics", "Electronics", "Electronics",
                     "Electronics", "Accessories", "Electronics", "Electronics"],
        "Quantity": [2, 5, 3, 1, 8, 15, 3, 4],
        "Price": [999.99, 699.99, 449.99, 999.99,
                  699.99, 79.99, 999.99, 449.99],
        "Region": ["North", "South", "East", "West",
                   "North", "South", "East", "North"]
    }
    df = pd.DataFrame(data)
    df["Revenue"] = df["Quantity"] * df["Price"]
    df.to_csv("sales_data.csv", index=False)
    print("Sample data created: sales_data.csv")
    return df


def load_data(filename="sales_data.csv"):
    """Load sales data from CSV"""
    if not os.path.exists(filename):
        print(f"{filename} not found. Creating sample data...")
        return create_sample_data()

    df = pd.read_csv(filename)
    df["Date"] = pd.to_datetime(df["Date"])
    if "Revenue" not in df.columns:
        df["Revenue"] = df["Quantity"] * df["Price"]
    return df


def show_summary(df):
    """Display overall sales summary"""
    print(f"\n{'=' * 40}")
    print(f"  SALES SUMMARY")
    print(f"{'=' * 40}")
    print(f"  Total Revenue:     ${df['Revenue'].sum():>12,.2f}")
    print(f"  Total Units Sold:  {df['Quantity'].sum():>12,}")
    print(f"  Average Order:     ${df['Revenue'].mean():>12,.2f}")
    print(f"  Number of Orders:  {len(df):>12,}")
    print(f"{'=' * 40}")


def show_by_product(df):
    """Revenue breakdown by product"""
    summary = df.groupby("Product").agg(
        Revenue=("Revenue", "sum"),
        Units=("Quantity", "sum"),
        Orders=("Revenue", "count")
    ).sort_values("Revenue", ascending=False)

    print(f"\n{'Product':<15} {'Revenue':>12} {'Units':>8} {'Orders':>8}")
    print("-" * 45)
    for product, row in summary.iterrows():
        print(f"{product:<15} ${row['Revenue']:>11,.2f} {row['Units']:>8} {row['Orders']:>8}")


def show_by_region(df):
    """Revenue breakdown by region"""
    summary = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    total = summary.sum()

    print(f"\n{'Region':<12} {'Revenue':>12} {'Share':>8}")
    print("-" * 35)
    for region, revenue in summary.items():
        pct = (revenue / total) * 100
        print(f"{region:<12} ${revenue:>11,.2f} {pct:>6.1f}%")


def export_report(df):
    """Export summary report to CSV"""
    summary = df.groupby("Product").agg(
        Revenue=("Revenue", "sum"),
        Units=("Quantity", "sum"),
        Avg_Price=("Price", "mean")
    ).round(2)
    filename = "sales_report.csv"
    summary.to_csv(filename)
    print(f"Report saved to {filename}")


# Main program
print("=" * 40)
print("  SALES DATA ANALYZER")
print("=" * 40)

df = load_data()

while True:
    print("\n1. Overall Summary")
    print("2. By Product")
    print("3. By Region")
    print("4. Export Report")
    print("5. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        show_summary(df)
    elif choice == "2":
        show_by_product(df)
    elif choice == "3":
        show_by_region(df)
    elif choice == "4":
        export_report(df)
    elif choice == "5":
        print("Goodbye!")
        break
