import pandas as pd
import mysql.connector

def load_data():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rajesh@1234",
        database="orders_db"
    )


    df_orders = pd.read_sql("SELECT * FROM orders", conn)
    df_order_items = pd.read_sql("SELECT * FROM order_items", conn)


    conn.close()

    return df_orders, df_order_items

if __name__ == "__main__":
    df_orders, df_order_items = load_data()
    print("Orders table sample:")
    print(df_orders.head())
    print("\nOrder items table sample:")
    print(df_order_items.head())