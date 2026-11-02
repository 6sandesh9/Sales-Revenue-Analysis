
# Sales & Revenue Analysis 

## Project Overview

This project focuses on analyzing sales data to understand revenue trends, profitability, product performance, and customer behavior.

An interactive dashboard was developed using Python and Streamlit to present key business insights through visualizations and interactive filters.

## Problem Statement

Businesses generate large amounts of sales data, but understanding overall sales performance, revenue trends, profitability, and customer purchasing behavior can be challenging without proper analysis and visualization.

This project aims to address this by analyzing the Superstore sales dataset and presenting important business information through an interactive dashboard. It helps users explore sales performance across different years, regions, product categories, and customer segments

## Objectives

- To explore the Superstore sales dataset.
- To clean and prepare the data.
- To analyze revenue and profit trends.
- To identify top-performing products and customers.
- To develop an interactive dashboard.

## Dataset

- **Dataset:** Superstore Sales Dataset
- **Records:** 9,994 rows
- **Columns:** 22
- **Description:** Contains order details, customer information, product categories, sales, quantity, discount, and profit.

## Tools & Technologies

- **Python** – Data analysis and processing
- **Pandas** – Data cleaning and manipulation
- **Matplotlib** – Data visualization
- **Streamlit** – Interactive dashboard development
- **Jupyter Notebook** – Data exploration and analysis

## Project Workflow

1. Loaded the Superstore dataset using Pandas.
2. Explored the dataset to understand its structure and identify data quality issues.
3. Cleaned and prepared the data for analysis.
4. Analyzed sales, revenue, profit, products, regions, and customer segments.
5. Created visualizations using Matplotlib.
6. Developed an interactive dashboard using Streamlit.

## Dashboard Features

### Key Performance Indicators (KPIs)

- Total Revenue
- Total Profit
- Total Orders
- Total Customers
- Average Order Value
- Profit Margin

### Visualizations

- Monthly Revenue Trend
- Revenue by Category and Region
- Top 10 Products by Revenue
- Top 10 Customers by Revenue
- Profit by Category
- Revenue Contribution by Customer Segment

### Interactive Features

- Filters for Year, Region, Category, and Customer Segment
- Download filtered sales data as a CSV file

## Project Structure

```text
Sales & Revenue Analysis/
│
├── Data/
│   ├── cleaned_superstore.csv
│   └── Superstore.csv
│
├── Modules/
│   ├── app.ipynb
│   ├── cleaned_superstore.csv
│   ├── data_cleaning.ipynb
│   └── sales_analysis.ipynb
│
├── Reports/
│   ├── monthly_revenue.png
│   ├── profit_by_products.png
│   ├── profit_distribution.png
│   ├── rev_by_category.png
│   ├── rev_by_region.png
│   ├── rev_contribution_customer_seg.png
│   ├── sales_distribution.png
│   ├── top10_customers_by_rev.png
│   ├── top10_products.png
│   └── yearly_revenue.png
│
├── Sales Analysis Dashboard/
│   └── app.py
│
├── app.py
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/6sandesh9/Sales-Revenue-Analysis.git
```

### 2. Navigate to the Project Folder

```bash
cd "Sales & Revenue Analysis"
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

Alternatively, install the libraries manually:

```bash
pip install streamlit pandas matplotlib numpy
```

### 4. Run the Dashboard

If `app.py` is in the main project folder:

```bash
python -m streamlit run app.py
```

If `app.py` is inside the `Sales Analysis Dashboard` folder:

```bash
python -m streamlit run "Sales Analysis Dashboard/app.py"
```

## Charts

### Monthly Revenue
![Monthly Revenue](Reports\monthly_revenue.png)

### Profit by product
![Profit by Product](Reports\profit_by_product.png)

### Profit Distribution
![Prodit Distribution](Reports\profit_distribution.png)


## Learning Outcomes

- Practiced data cleaning and exploratory data analysis.
- Improved understanding of sales and profitability metrics.
- Gained experience creating visualizations with Matplotlib.
- Developed an interactive dashboard using Streamlit.
- Practiced organizing and documenting a data analytics project.
