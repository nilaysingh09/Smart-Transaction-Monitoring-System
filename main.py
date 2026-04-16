import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("transactions.csv")

# Rule 1: High amount
df["high_risk"] = df["amount"] > 10000

# Rule 2: Frequent transactions
df["frequent"] = df["transactions_per_day"] > 3

# Final decision
df["is_suspicious"] = df["high_risk"] | df["frequent"]

print(df)

# Save results
df.to_csv("output.csv", index=False)




# Visualizations

df["is_suspicious"].value_counts().plot(kind='bar')
plt.title("Suspicious vs Normal Transactions")
plt.show()
