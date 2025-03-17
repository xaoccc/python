import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery = delivery.sort_values(by=['customer_id', 'order_date']).drop_duplicates(subset='customer_id', keep='first')
    delivery['immediate_percentage'] = (delivery.customer_pref_delivery_date - delivery.order_date).apply(lambda x: 0 if  x == pd.Timedelta(0) else 1)
    percentage = delivery['immediate_percentage'].mean()*100
    return pd.DataFrame({'immediate_percentage': [100 - percentage]}).round(2)