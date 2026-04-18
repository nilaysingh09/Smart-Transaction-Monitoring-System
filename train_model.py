import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/transactions.csv")

# Features and target
X = df[["amount", "transactions_per_day"]]
y = df["is_fraud"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Predict
prediction = model.predict([[20000, 10]])

print("Prediction:", "Fraud" if prediction[0] == 1 else "Safe")
