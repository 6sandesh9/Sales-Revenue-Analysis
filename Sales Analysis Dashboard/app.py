
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page Configuration

st.set_page_config(
    page_title="Sales Analysis Dashboard",
    layout="wide"
)

# 2. Load Dataset

@st.cache_data
def load_data():
    df = pd.read_csv(
        r"D:\Sales & Revenue Analysis\Data\cleaned_superstore.csv"
    )
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# 3. Dashboard Title

st.title("Sales and Revenue Analysis Dashboard")
st.write("Explore sales, profit, products and customer performance.")

st.divider()

# 4. Sidebar Filters

st.sidebar.header("Dashboard Filters")

years = sorted(df["Year"].dropna().unique())
selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + years
)

regions = sorted(df["Region"].dropna().unique())
selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + regions
)

categories = sorted(df["Category"].dropna().unique())
selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + categories
)

segments = sorted(df["Segment"].dropna().unique())
selected_segment = st.sidebar.selectbox(
    "Select Customer Segment",
    ["All"] + segments
)

# 5. Apply Filters

filtered_df = df.copy()

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]

# 6. Calculate KPIs

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_customers = filtered_df["Customer ID"].nunique()

avg_order_value = (
    total_sales / total_orders if total_orders > 0 else 0
)

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales != 0 else 0
)

# 7. Display KPIs

st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col5.metric(
    "Average Order Value",
    f"${avg_order_value:,.2f}"
)

col6.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

st.divider()

# 8. Monthly Revenue Trend

st.subheader("Monthly Revenue Trend")

monthly_sales = (
    filtered_df.groupby("Year-Month")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Year-Month")
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly_sales["Year-Month"],
    monthly_sales["Sales"],
    marker="o"
)

ax.set_title("Monthly Revenue Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.tick_params(axis="x", rotation=45)
ax.grid(True)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 9. Category and Regional Analysis

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Category")

    category_sales = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.bar(
        category_sales.index,
        category_sales.values
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Product Category")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.subheader("Revenue by Region")

    region_sales = (
        filtered_df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.bar(
        region_sales.index,
        region_sales.values,
        edgecolor="black"
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Region")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# 10. Top 10 Products

st.subheader("Top 10 Products by Revenue")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(12, 6))

ax.barh(
    top_products.index,
    top_products.values
)

ax.set_xlabel("Revenue")
ax.set_ylabel("Product Name")
ax.set_title("Top 10 Products")

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# customer by revenue
st.subheader("Top 10 Customers by Revenue")

top_customers = (
    filtered_df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(12, 6))

ax.barh(
    top_customers.index,
    top_customers.values
)

ax.set_xlabel("Revenue")
ax.set_ylabel("Customer Name")
ax.set_title("Top 10 Customers by Revenue")

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 11. Profit by Category

st.subheader("Profit by Product Category")

category_profit = (
    filtered_df.groupby("Category")["Profit"]
    .sum()
)

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    category_profit.index,
    category_profit.values
)

ax.set_xlabel("Category")
ax.set_ylabel("Profit")
ax.set_title("Profit by Category")
ax.axhline(0, linewidth=0.8)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 12. Customer Segment Analysis

st.subheader("Revenue Contribution by Customer Segment")

segment_sales = (
    filtered_df.groupby("Segment")["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(7, 7))

ax.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Customer Segment Revenue")

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 13. Data Table

st.subheader("Sales Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# 14. Download Filtered Data

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="DOWNLOAD FILTERED DATA",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.success("Dashboard loaded successfully!")
