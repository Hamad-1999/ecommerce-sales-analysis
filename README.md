# E-commerce Sales Analysis

## Project Overview

This project analyzes a small e-commerce sales dataset using Python and Pandas.

The goal is to demonstrate a complete data-analysis workflow:

* Loading raw CSV data
* Data cleaning and transformation
* Feature engineering
* KPI analysis
* Business analysis
* Report generation
* Data visualization

> **Note:** The dataset is synthetic and created for learning and portfolio practice.

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* CSV
* VS Code

## Project Structure

```text
04_pandas_project/
│
├── data/
│   └── sales_data.csv
│
├── output/
│   ├── processed_sales_data.csv
│   ├── kpi_report.csv
│   ├── sales_by_category.csv
│   ├── sales_by_month.csv
│   ├── sales_by_city.csv
│   ├── top_3_customers.csv
│   └── top_3_products.csv
│
├── charts/
│   ├── sales_by_category.png
│   ├── sales_by_month.png
│   ├── sales_by_city.png
│   ├── top_3_products.png
│   └── top_3_customers.png
│
├── sales_analysis.py
└── README.md
```

## Key KPIs

| KPI                 |  Value |
| ------------------- | -----: |
| Total Sales         | €5,260 |
| Total Orders        |     10 |
| Average Order Value |   €526 |
| Total Units Sold    |     24 |

## Key Business Insights

### Sales by Category

Electronics generated the highest sales:

* Electronics: €3,860
* Furniture: €1,400

Electronics represented approximately 73.38% of total sales.

### Sales by City

* Brussels: €3,200
* Ghent: €1,150
* Antwerp: €910

Brussels generated the highest total sales.

### Top Products

The top 3 products by total sales were:

1. Laptop — €2,750
2. Desk — €800
3. Chair — €600

### Top Customers

The top 3 customers by total sales were:

1. Ali — €1,800
2. Mona — €950
3. Lina — €800

### Monthly Sales

* January: €3,325
* February: €1,935

Sales decreased from January to February by approximately 41.8%.

## Important Business Insight

The product with the highest number of units sold was **Mouse**, with 8 units.

However, **Laptop** generated the highest revenue with only 3 units sold.

This demonstrates that sales volume and revenue are not the same metric.

## How to Run

Make sure Python is installed and the project virtual environment is activated.

Install the required packages:

```bash
pip install pandas matplotlib
```

Run the analysis:

```bash
python sales_analysis.py
```

The script will:

1. Load the raw sales data.
2. Convert and clean the data.
3. Create calculated fields such as `Total_Sales` and `Month`.
4. Perform business analysis.
5. Generate CSV reports.
6. Generate visualization images.

## Project Goal

This project is part of a practical learning path toward Data Analyst / Data Scientist roles.

Future improvements may include:

* SQL analysis
* Power BI dashboard
* Larger real-world datasets
* Advanced exploratory data analysis
* Machine Learning
* Interactive dashboards
