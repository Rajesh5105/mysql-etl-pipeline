import pandas as pd

def transformation_data(orders_df, order_items_df):

    cancelled_orders_df = orders_df[orders_df['status'] == 'Cancelled']
    active_orders_df = orders_df[orders_df['status'] != 'Cancelled']

    order_summary = {
        'cancelled_df': cancelled_orders_df,
        'active_df': active_orders_df,
        'cancelled_count': len(cancelled_orders_df),
        'active_count': len(active_orders_df)
    }

    merged_df = pd.merge(active_orders_df, order_items_df, how='inner', on='order_id')


    merged_df['line_revenue'] = merged_df['quantity'] * merged_df['unit_price']
    merged_df['discounted_revenue'] = merged_df['line_revenue'] * (1 - merged_df['discount_pct'] / 100)
    merged_df['discounted_revenue'] = merged_df['discounted_revenue'].round(2)

 
    customer_summary = merged_df.groupby('customer_id').agg(
        total_orders=('order_id', 'nunique'),
        total_items_purchased=('quantity', 'sum'),
        total_revenue=('discounted_revenue', 'sum')
    ).reset_index()
    customer_summary = customer_summary.sort_values(by='total_revenue', ascending=False)
    customer_summary['rank'] = range(1, len(customer_summary) + 1)


    product_summary = merged_df.groupby('product_id').agg(
        total_units_sold=('quantity', 'sum'),
        total_revenue=('discounted_revenue', 'sum')
    ).reset_index()
    product_summary = product_summary.sort_values(by='total_units_sold', ascending=False)

    daily_summary = merged_df.groupby('order_date').agg(
        total_orders=('order_id', 'nunique'),
        total_revenue=('discounted_revenue', 'sum')
    ).reset_index()

    return customer_summary, product_summary, daily_summary, order_summary


if __name__ == "__main__":
    from extract import load_data 
    orders_df, order_items_df = load_data()
    cust, prod, daily, canc = transformation_data(orders_df, order_items_df)

    print("Customer Summary:")
    print(cust.head())
    print("\nProduct Summary:")
    print(prod.head())
    print("\nDaily Summary:")
    print(daily.head())
    print("\nCancelled Orders Count:")
    print(canc['cancelled_count'])