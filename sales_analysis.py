# ==========================================
# 1. Imports
# ==========================================

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 2. Load Data
# ==========================================

project_folder = Path(__file__).resolve().parent

df = pd.read_csv(
    project_folder / "data" / "sales_data.csv"
)

print("\n--- Raw Data ---")
print(df)


# ==========================================
# 3. Data Cleaning & Feature Engineering
# ==========================================

# تحويل التاريخ من نص إلى datetime
df["Date"] = pd.to_datetime(df["Date"])

# حساب إجمالي مبيعات كل طلب
df["Total_Sales"] = df["Quantity"] * df["Price"]

# استخراج رقم الشهر
df["Month"] = df["Date"].dt.month

# استخراج اسم الشهر
df["Month_Name"] = df["Date"].dt.month_name()

print("\n--- Processed Data ---")
print(df)


# ==========================================
# 4. KPI Analysis
# ==========================================

total_sales = df["Total_Sales"].sum()

total_orders = df["Order_ID"].nunique()

average_order_value = df["Total_Sales"].mean()

total_units = df["Quantity"].sum()


kpi_report = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Orders",
        "Average Order Value",
        "Total Units Sold"
    ],
    "Value": [
        total_sales,
        total_orders,
        average_order_value,
        total_units
    ]
})

print("\n--- KPI Report ---")
print(kpi_report)


# ==========================================
# 5. Business Analysis
# ==========================================

# ------------------------------------------
# المبيعات حسب الفئة
# ------------------------------------------

category_report = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .reset_index()
)

print("\n--- Sales by Category ---")
print(category_report)


# ------------------------------------------
# المبيعات حسب الشهر
# ------------------------------------------

monthly_report = (
    df.groupby(["Month", "Month_Name"])["Total_Sales"]
    .sum()
    .reset_index()
)

print("\n--- Sales by Month ---")
print(monthly_report)


# ------------------------------------------
# المبيعات حسب المدينة
# ------------------------------------------

city_report = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .reset_index()
)

print("\n--- Sales by City ---")
print(city_report)


# ------------------------------------------
# أفضل 3 عملاء
# ------------------------------------------

top_customers_report = (
    df.groupby("Customer")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
    .reset_index()
)

print("\n--- Top 3 Customers ---")
print(top_customers_report)


# ------------------------------------------
# أفضل 3 منتجات
# ------------------------------------------

top_products_report = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
    .reset_index()
)

print("\n--- Top 3 Products ---")
print(top_products_report)


# ==========================================
# 6. Save Reports
# ==========================================

output_folder = project_folder / "output"

output_folder.mkdir(exist_ok=True)

# البيانات المعالجة
df.to_csv(
    output_folder / "processed_sales_data.csv",
    index=False
)

# KPI
kpi_report.to_csv(
    output_folder / "kpi_report.csv",
    index=False
)

# المبيعات حسب الفئة
category_report.to_csv(
    output_folder / "sales_by_category.csv",
    index=False
)

# المبيعات حسب الشهر
monthly_report.to_csv(
    output_folder / "sales_by_month.csv",
    index=False
)

# المبيعات حسب المدينة
city_report.to_csv(
    output_folder / "sales_by_city.csv",
    index=False
)

# أفضل 3 عملاء
top_customers_report.to_csv(
    output_folder / "top_3_customers.csv",
    index=False
)

# أفضل 3 منتجات
top_products_report.to_csv(
    output_folder / "top_3_products.csv",
    index=False
)

print("\nAll reports have been saved successfully.")


# ==========================================
# 7. Visualizations
# ==========================================

charts_folder = project_folder / "charts"
charts_folder.mkdir(exist_ok=True)


# ------------------------------------------
# Sales by Category
# ------------------------------------------


plt.figure(figsize=(8, 5))

bars = plt.bar(
    category_report["Category"],
    category_report["Total_Sales"]
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (€)")

plt.bar_label(bars, fmt="€%.0f", padding=3)

plt.tight_layout()

plt.savefig(
    charts_folder / "sales_by_category.png"
)

plt.show()


# ------------------------------------------
# Monthly Sales Trend
# ------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    monthly_report["Month_Name"],
    monthly_report["Total_Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (€)")

plt.tight_layout()

plt.savefig(
    charts_folder / "sales_by_month.png"
)

plt.show()

# ------------------------------------------
# Sales by City
# ------------------------------------------

plt.figure(figsize=(8, 5))

bars = plt.bar(
    city_report["City"],
    city_report["Total_Sales"]
)

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales (€)")

plt.bar_label(bars, fmt="€%.0f", padding=3)

plt.tight_layout()

plt.savefig(
    charts_folder / "sales_by_city.png"
)

plt.show()


# ------------------------------------------
# Top 3 Products by Sales
# ------------------------------------------

plt.figure(figsize=(8, 5))

bars = plt.bar(
    top_products_report["Product"],
    top_products_report["Total_Sales"]
)

plt.title("Top 3 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales (€)")

plt.bar_label(bars, fmt="€%.0f", padding=3)

plt.tight_layout()

plt.savefig(
    charts_folder / "top_3_products.png"
)

plt.close()


# ------------------------------------------
# Top 3 Customers by Sales
# ------------------------------------------

plt.figure(figsize=(8, 5))

bars = plt.bar(
    top_customers_report["Customer"],
    top_customers_report["Total_Sales"]
)

plt.title("Top 3 Customers by Sales")
plt.xlabel("Customer")
plt.ylabel("Sales (€)")

plt.bar_label(bars, fmt="€%.0f", padding=3)

plt.tight_layout()

plt.savefig(
    charts_folder / "top_3_customers.png"
)

plt.close()