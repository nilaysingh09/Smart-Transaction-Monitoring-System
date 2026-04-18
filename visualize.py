import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/transactions.csv")

# 1. Fraud vs Non-Fraud Count
df['is_fraud'].value_counts().plot(kind='bar')
plt.title("Fraud vs Normal Transactions")
plt.xlabel("Class (0 = Normal, 1 = Fraud)")
plt.ylabel("Count")
plt.show()


# 2. Amount Distribution
plt.hist(df['amount'], bins=5)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()


# 3. Transactions per Day vs Fraud
plt.scatter(df['transactions_per_day'], df['amount'])
plt.title("Transactions vs Amount")
plt.xlabel("Transactions per Day")
plt.ylabel("Amount")
plt.show()
