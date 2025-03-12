import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    accepted_count = request_accepted.groupby(by='requester_id', as_index=False).count()[['requester_id', 'accepter_id']].rename(columns={'requester_id': 'id'})
    request_count = request_accepted.groupby(by='accepter_id', as_index=False).count()[['requester_id', 'accepter_id']].rename(columns={'accepter_id': 'id'})
    result = accepted_count.merge(request_count, on='id', how='outer').fillna(0)
    result['num'] = result.accepter_id + result.requester_id
    return result[['id', 'num']].sort_values(by='num', ascending=False).head(1)