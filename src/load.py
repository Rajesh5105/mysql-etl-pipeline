from sqlalchemy import create_engine

def load_to_mysql(df, table_name):

    engine = create_engine(
        "mysql+mysqlconnector://root:Rajesh%401234@localhost/orders_db"
    )

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False
    )

    print(f"Loaded {len(df)} rows into {table_name}")



if __name__ == "__main__":
    from extract import load_data
    from transform import transformation_data


    orders_df, order_items_df = load_data()

 
    customer_summary, product_summary, daily_summary, order_summary = transformation_data(orders_df, order_items_df)

 
    load_to_mysql(customer_summary, "customer_revenue")
    load_to_mysql(product_summary, "product_revenue")
    load_to_mysql(daily_summary, "daily_revenue")
    load_to_mysql(order_summary['cancelled_df'], "cancellation_report")

    print("ETL completed successfully ")