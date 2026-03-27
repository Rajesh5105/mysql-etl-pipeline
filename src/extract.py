import pandas as pd
import mysql.connector

def customer_dim():
    # Create connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rajesh@1234",
        database="orders_db"
    )

    dim_df = pd.read_sql("SELECT * FROM dim_customer", conn)
    updates_df = pd.read_csv(r"C:\Users\hp\Desktop\ppp\scdtypo1\src\customer_updates.csv")
    conn.close()
    return dim_df, updates_df
dim_df, updates_df = customer_dim()
print(dim_df.head())
print(updates_df.head())

