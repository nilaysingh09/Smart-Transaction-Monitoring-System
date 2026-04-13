import pandas as pd

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
