import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# File Info
df = pd.read_csv('Stores.csv')
print(df.info())

# File Head
print(df.head())

# Null Values In File
print(df.isnull().sum())

# Duplicated Values
print(df.duplicated())

"""EXPLORATORY DATA ANALYSIS"""

print(df.describe())

df['total_monthly_customers_count'] = df['Daily_Customer_Count'] * 30
df['avg_customer_spend_day'] = df['Store_Sales'] / df['total_monthly_customers_count']
df['avg_customer_spend_month'] = df['Store_Sales'] / df['Daily_Customer_Count']
df['avg_daily_sales'] = df['Store_Sales'] / 30

print(df.head())

# Graph 1

df.Daily_Customer_Count.hist(bins=50, figsize=(12, 8))
plt.show()

# Graph 2

df.hist(figsize=(12, 8))
plt.grid(False)

# Graph 3

# Correlation Data
correlation = df.corr()
print(correlation['Store_Sales'].sort_values(ascending=False), '\n')

k = 10
cols = correlation.nlargest(k, 'Store_Sales')['Store_Sales'].index
cm = np.corrcoef(df[cols].values.T)
f, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(cm, vmax=.8, linewidths=0.01, square=True, annot=True, cmap="YlGnBu",
            linecolor="b", xticklabels=cols.values, annot_kws={'size': 12}, yticklabels=cols.values)
plt.show()

# Graph 4

fac = df["Store_Sales"]
fac1 = df["Daily_Customer_Count"]
plt.figure(figsize=(12, 8))
plt.scatter(fac1, fac, s=15)
plt.xlabel('Count of Customers')
plt.ylabel('Sales in $')
plt.title('Customers & Sales of All Stores')
plt.xlim(200, 2000)
plt.yscale("linear")
plt.grid(True)

# Graph 5

x = df[['Items_Available']]
y = df[['Store_Sales']]
_ = plt.figure(figsize=(12, 8))
_ = plt.scatter(x, y)
_ = plt.xlabel('Items Available')
_ = plt.ylabel('Sales')
_ = plt.xticks(np.arange(0, 2800, step=200))
_ = plt.yticks(np.arange(0, 120000, step=20000), ['20K', '40K', '60K', '80K', '100K', '120K'])
plt.plot()

# Sorted Data

print(df.sort_values('Store_Sales', ascending=False))
