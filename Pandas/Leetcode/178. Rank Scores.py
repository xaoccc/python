import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if scores.size == 0:
        return pd.DataFrame([], columns=('score', 'rank'))
    sorted_values = scores.sort_values(['score'], ascending=False)['score'].reset_index(drop=True)
    rows = sorted_values.size
    rank = pd.Series([])
    start = 1
    rank[0] = 1
    for i in range(1, rows):
        if sorted_values[i] != sorted_values[i - 1]:
            start += 1
        rank[i] = start
    scores['score'] = sorted_values
    scores['rank'] = rank

    return scores.loc[:,['score', 'rank']]