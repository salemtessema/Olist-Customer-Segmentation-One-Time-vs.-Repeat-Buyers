#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:16:53 2026

@author: salemt
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#upload data 
df = pd.read_csv('/Users/salemt/Downloads/Olist data.csv')

#checking nulls
df.isnull().sum()

#converting first & last purchase to datetime
df[["first_purchase", "last_purchase"]] = df[["first_purchase", "last_purchase"]].apply(pd.to_datetime)

#filling product and shipping value with 0
df["total_product_value"] = df["total_product_value"].fillna(0)
df["total_shipping_value"] = df["total_shipping_value"].fillna(0)

#customer segmentation
df['customer_segmentation'] = df['total_orders'].apply(lambda x: 'One-time' if x==1 else 'Repeat')

#comparison 
df.groupby('customer_segmentation')[['total_product_value', 'total_payment_value', 'average_review_score']].mean().round(2).T

#Revenue by customer segment
rev = df.groupby('customer_segmentation')['total_payment_value'].sum()
print((rev / rev.sum() *100).round(1))

plt.bar(rev.index, rev.values)
plt.title('Revenue by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Total Payment Value ($)')
plt.show()

#plotting average spend by customer 
avg = df.groupby('customer_segmentation')['total_payment_value'].mean()
plt.bar(avg.index, avg.values)
plt.title('Average Spend by Customer Segment')
plt.xlabel('')
plt.ylabel('Total Payment Value ($)')
plt.show()


#Percentage of Reviews by customer segments
df['has_review'] = df['average_review_score'].notnull()
df.groupby('customer_segmentation')['has_review'].mean().round(2)

#how long does it take for returning customes to make another purchase
repeat = df[df['customer_segmentation'] == 'Repeat'].copy()
repeat['days_between'] = (repeat['last_purchase'] - repeat['first_purchase']).dt.days
repeat['days_between'].describe()

#histogram of days_between for repeat customers
plt.boxplot(repeat['days_between'])
plt.title('Days Between First Purchase and Last Purchase (Repeat Customers Only)')
plt.xlabel('Days')
plt.show()
