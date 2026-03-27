from src.extract import load_data
from src.transform import transformation_data
from src. load import load_to_mysql

def main():
    print("Reading data.....")
    orders_df, order_items_df = load_data() 

    print("Transforming data.......")
    customer_summary, product_summary, daily_summary, order_summary = transformation_data(orders_df, order_items_df)

    print("Loading data......")
    load_to_mysql(customer_summary, "customer_revenue")
    load_to_mysql(product_summary, "product_revenue")
    load_to_mysql(daily_summary, "daily_revenue")
    load_to_mysql(order_summary['cancelled_df'], "cancellation_report")  # load only cancelled orders

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()