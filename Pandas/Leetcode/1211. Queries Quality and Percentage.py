import pandas as pd


# def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
#     queries.drop(columns=['result'], inplace=True)
#     queries['quality'] = (queries['rating'] / queries['position'])
#
#     counts_total = queries['query_name'].value_counts()
#
#     low_ratings = queries.loc[queries['rating'] < 3, :]
#     counts_low = low_ratings['query_name'].value_counts()
#
#     queries['poor_query_percentage'] = queries['query_name'].map((counts_low / counts_total) * 100).round(2)
#
#     queries = queries.groupby(by='query_name', as_index=False).mean()
#     queries['quality'] = queries['quality'].round(2)
#     queries['poor_query_percentage'].fillna(0, inplace=True)
#
#     return queries.drop(columns=['position', 'rating'])

import pandas as pd
# Function to reduce bias when used round(2)
round2 = lambda x: round(x + 1e-9, 2)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries.rating/queries.position
    # queries.rating < 3 alone returns a bool, but in the math context (queries.rating < 3)*100 the bool is cast
    # to int so values in the column will be either 100 or 0.
    queries['poor_query_percentage'] = (queries.rating < 3)*100

    return queries.groupby(by='query_name')[['quality',
          'poor_query_percentage']].mean().apply(round2).reset_index()