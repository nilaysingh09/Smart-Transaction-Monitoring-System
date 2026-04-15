import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass",
    database="frauddetection"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    user_id INT,
    amount FLOAT,
    transactions_per_day INT
)
""")

print("Table created successfully")
