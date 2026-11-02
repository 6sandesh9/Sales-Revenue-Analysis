Sales \& Revenue Analysis Dashboard



Project Overview



This project focuses on analyzing sales data to understand revenue trends, profitability, product performance, and customer behavior. An interactive dashboard was developed using Python and Streamlit to present key business insights through visualizations and interactive filters.



Dataset



Dataset: Superstore Sales Dataset



Records: 9,994 rows



Columns: 22



Contains order details, customer information, product categories, sales, quantity, discount, and profit.



Tools \& Technologies



Python – Data analysis and processing



Pandas – Data cleaning and manipulation



Matplotlib – Data visualization



Streamlit – Interactive dashboard development



Jupyter Notebook – Data exploration and analysis



Project Workflow



Loaded the Superstore dataset using Pandas.



Explored the dataset to understand its structure and identify data quality issues.



Cleaned and prepared the data for analysis.



Analyzed sales, revenue, profit, products, regions, and customer segments.



Created visualizations using Matplotlib.



Developed an interactive dashboard using Streamlit.



Dashboard Features



Key performance indicators (KPIs):



Total Revenue



Total Profit



Total Orders



Total Customers



Average Order Value



Profit Margin



Monthly Revenue Trend



Revenue by Category and Region



Top 10 Products by Revenue



Top 10 Customers by Revenue



Profit by Category



Revenue Contribution by Customer Segment



Interactive filters for Year, Region, Category, and Customer Segment



Download filtered sales data as a CSV file



Project Structure



Sales \& Revenue Analysis/

│

├── Data/

│   └── cleaned\_superstore.csv

│   └── Superstore.csv

│

├── Modules/

│   └── app.ipynb

│   └── cleaned\_superstore.csv

│   └── data\_cleaning.ipynb

│   └── sales\_analysis.ipynb

│

├── Reports/

│   └── monthly\_revenue.png

│   └── profit\_by\_products.png

│   └── profit\_distribution.png

│   └── rev\_by\_category.png

│   └── rev\_by\_region.png

│   └── rev\_contribution\_customer\_seg.png

│   └── sales\_distribution.png

│   └── top10\_customers\_by\_rev.png

│   └── top10\_products.png

│   └── yearly\_revenue.png

│

├── Sales Analysis Dashboard/

│   └── app.py

│

├── app.py

│

├── requirements.txt

│

└── README.md



How to Run the Project



Clone this repository:



git clone https://github.com/6sandesh9/your-repository-name.git



Navigate to the project folder:



cd "Sales \& Revenue Analysis"



Install the required libraries:



pip install streamlit pandas matplotlib numpy



Run the dashboard:



python -m streamlit run app.py



Learning Outcomes



Practiced data cleaning and exploratory data analysis.



Improved understanding of sales and profitability metrics.



Gained experience creating visualizations with Matplotlib.



Developed an interactive dashboard using Streamlit.



Practiced organizing and documenting a data analytics project.

