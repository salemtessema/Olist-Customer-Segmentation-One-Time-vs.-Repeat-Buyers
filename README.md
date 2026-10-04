# Olist Customer Segmentation Analysis

## Overview

This project analyzes customer purchasing behavior using the **Olist Brazilian E-Commerce Dataset**. I used SQL to build a customer-level dataset from multiple relational tables and Python to clean, analyze, and visualize the data. The goal was to compare one-time and repeat customers to better understand spending patterns, revenue contribution, customer satisfaction, and purchasing behavior.

---

## Project Objectives

- Build a customer-level dataset from multiple Olist tables using SQL.
- Segment customers into one-time and repeat buyers.
- Compare total revenue and average spending between customer segments.
- Analyze customer review behavior.
- Examine purchasing timelines for repeat customers.
- Visualize key business insights.

---

## Tools Used

- **SQL (MySQL)**
- **Python**
  - pandas
  - matplotlib
  - seaborn

---

## Dataset

This project uses the **Olist Brazilian E-Commerce Public Dataset**, which contains information on customers, orders, order items, payments, and reviews.

---

## Methodology

### 1. Data Extraction (SQL)

I used SQL to combine data from the Olist customer, orders, payments, reviews, and order items tables into a customer-level dataset. Using Common Table Expressions (CTEs), I calculated:

- Total orders
- First and last purchase dates
- Total product value
- Total shipping value
- Total payment value
- Average review score

After creating the dataset, I exported the results as a CSV for analysis in Python.

### 2. Data Preparation (Python)

Next, I imported the CSV into Python and prepared it for analysis by:

- Converting purchase dates to datetime format
- Filling missing values where appropriate
- Segmenting customers into:
  - **One-time:** 1 purchase
  - **Repeat:** 2 or more purchases

### 3. Exploratory Data Analysis

Once the data was cleaned, I compared one-time and repeat customers across several business metrics, including:

- Total revenue
- Average spending per customer
- Customer review scores
- Review participation
- Time between a repeat customer's first and last purchase

I used Python to create visualizations that highlight the differences between the two customer segments.

---

## Key Findings

- **One-time customers generated most of the total revenue.** While repeat customers spent more on average, one-time customers contributed a larger share of overall revenue because they made up a much larger portion of the customer base.

- **Repeat customers spent significantly more per customer.** On average, repeat customers had a much higher total payment value than one-time customers, making them more valuable on an individual basis.

- **Customer satisfaction was similar across both groups.** Average review scores did not differ much between one-time and repeat customers.

- **Most repeat customers made their purchases within a relatively short time frame.** The distribution of days between a customer's first and last purchase was heavily right-skewed, with most customers purchasing again within a few months and a smaller group remaining active for much longer.

---

## Business Takeaways

- One-time customers currently drive most of the platform's revenue due to their larger numbers.
- Repeat customers spend more on average, making customer retention an opportunity to increase long-term revenue.
- Converting more one-time customers into repeat buyers could increase customer lifetime value.
- Long-term repeat customers may be good candidates for loyalty or targeted marketing campaigns.

---

## Repository Structure

```text
├── Olist Project.sql              # SQL query used to create the customer-level dataset
├── Olist data.csv                 # Customer-level dataset exported from SQL
├── Personal Project Olist Data.py # Python script for data cleaning, analysis, and visualizations
└── README.md
```

---

## Skills Demonstrated

- SQL joins and Common Table Expressions (CTEs)
- Data aggregation and transformation
- Data cleaning with pandas
- Exploratory Data Analysis (EDA)
- Customer segmentation
- Data visualization
- Business analytics
- Translating transactional data into actionable business insights

---

## Future Improvements

- Perform RFM (Recency, Frequency, Monetary) analysis
- Estimate customer lifetime value (CLV)
- Build an interactive dashboard in Tableau or Power BI
- Develop a predictive model for customer retention

---

## Author

**Salem**

Master's student in Data Science interested in data analytics and business intelligence. This project demonstrates an end-to-end analytics workflow, from querying relational data with SQL to performing exploratory analysis and generating business insights in Python.
