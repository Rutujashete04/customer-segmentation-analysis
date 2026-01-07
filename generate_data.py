import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 50,000 customer records
n_customers = 50000

# Customer ID
customer_ids = [f'CUST_{str(i).zfill(6)}' for i in range(1, n_customers + 1)]

# Age (18-80)
ages = np.random.normal(40, 15, n_customers).astype(int)
ages = np.clip(ages, 18, 80)

# Annual Income ($20K - $150K)
incomes = np.random.lognormal(10.8, 0.5, n_customers)
incomes = np.clip(incomes, 20000, 150000)

# Spending Score (1-100) - correlated with income
base_spending = (incomes - 20000) / 1300
noise = np.random.normal(0, 15, n_customers)
spending_scores = base_spending + noise
spending_scores = np.clip(spending_scores, 1, 100)

# Number of Purchases (0-100)
purchases = np.random.poisson(20, n_customers)
purchases = np.clip(purchases, 0, 100)

# Average Transaction Value ($10-$500)
avg_transaction = np.random.gamma(5, 20, n_customers)
avg_transaction = np.clip(avg_transaction, 10, 500)

# Customer Tenure (months) (1-120)
tenure = np.random.exponential(30, n_customers).astype(int)
tenure = np.clip(tenure, 1, 120)

# Website Visits per Month (0-50)
website_visits = np.random.negative_binomial(5, 0.3, n_customers)
website_visits = np.clip(website_visits, 0, 50)

# Email Open Rate (0-1)
email_open_rate = np.random.beta(2, 5, n_customers)

# Product Categories Purchased (1-10)
categories = np.random.randint(1, 11, n_customers)

# Last Purchase Days Ago (0-365)
days_since_purchase = np.random.exponential(60, n_customers).astype(int)
days_since_purchase = np.clip(days_since_purchase, 0, 365)

# Create DataFrame
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Age': ages,
    'Annual_Income': incomes,
    'Spending_Score': spending_scores,
    'Total_Purchases': purchases,
    'Avg_Transaction_Value': avg_transaction,
    'Tenure_Months': tenure,
    'Website_Visits_Monthly': website_visits,
    'Email_Open_Rate': email_open_rate,
    'Product_Categories': categories,
    'Days_Since_Last_Purchase': days_since_purchase
})

# Save to CSV
df.to_csv('data/customer_data.csv', index=False)
print(f"✅ Generated {len(df):,} customer records")
print("\n📊 First few rows:")
print(df.head())
print("\n📈 Dataset Info:")
print(df.info())
print("\n📉 Basic Statistics:")
print(df.describe())