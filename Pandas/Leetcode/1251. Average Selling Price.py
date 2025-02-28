import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    if len(units_sold) == 0 and len(prices) == 0:
        units_sold['average_price'] = pd.Series()
        return units_sold[['product_id', 'average_price']]
    if len(units_sold) == 0:
        prices['average_price'] = pd.Series(0, index=prices.index)
        return prices[['product_id', 'average_price']]

    units_sold = units_sold.groupby(by=["product_id", "purchase_date"], as_index=False).sum()
    print(units_sold)
    for index, row in units_sold.iterrows():
        prices_filtered = prices.loc[
            (prices['start_date'] <= row['purchase_date']) & (prices['end_date'] >= row['purchase_date']) & (
                        prices['product_id'] == row['product_id'])]

        if not prices_filtered.empty:
            price = prices_filtered['price'].iloc[0]
            units_sold.at[index, 'total_price'] = row['units'] * price
        else:
            units_sold.at[index, 'total_price'] = 0
    result = units_sold.drop(columns=['purchase_date']).groupby(by=['product_id'], as_index=False).sum()

    result['average_price'] = (result['total_price'] / result['units']).round(2)

    result = result[['product_id', 'average_price']]

    for index, row in prices.iterrows():
        if row['product_id'] not in result['product_id'].values:
            new_row = {'product_id': row['product_id'], 'average_price': 0}
            result = pd.concat([result, pd.DataFrame([new_row])], ignore_index=True)

    return result

