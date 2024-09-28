import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Get the valid companies and orders
    com_id_not_red = company.loc[(company.name != 'RED'), ['com_id']]
    valid_orders = orders[orders['com_id'].isin(com_id_not_red['com_id'])]

    # Get the invalid companies and sales id
    invalid_com_id = company.loc[(company.name == 'RED'), ['com_id']]
    invalid_sales_ids = orders.loc[orders['com_id'].isin(invalid_com_id['com_id']), ['sales_id']]

    # Filter the sales person by 3 criteria:
    # 1. Sales person who has no orders
    # 2. Sales person who has valid orders
    # 3. Remove all orders of sales persons who have invalid orders
    filtered_sales_person = sales_person[~sales_person['sales_id'].isin(orders['sales_id']) |
                            (sales_person['sales_id'].isin(valid_orders['sales_id']) &
                            ~sales_person['sales_id'].isin(invalid_sales_ids['sales_id']))]


    return filtered_sales_person[['name']]