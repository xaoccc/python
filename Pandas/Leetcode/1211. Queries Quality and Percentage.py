import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries.drop(columns=['result'], inplace=True)
    queries['quality'] = (queries['rating'] / queries['position'])

    counts_total = queries['query_name'].value_counts()

    low_ratings = queries.loc[queries['rating'] < 3, :]
    counts_low = low_ratings['query_name'].value_counts()

    queries['poor_query_percentage'] = queries['query_name'].map((counts_low / counts_total) * 100).round(2)

    queries = queries.groupby(by='query_name', as_index=False).mean()
    queries['quality'] = queries['quality'].round(2)
    queries['poor_query_percentage'].fillna(0, inplace=True)
    print(queries.drop(columns=['position', 'rating']))
    return queries.drop(columns=['position', 'rating'])