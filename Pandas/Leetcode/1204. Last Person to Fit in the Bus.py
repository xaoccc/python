import pandas as pd

# Python solution:
def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    result, total = '', 0
    queue.sort_values(by='turn', inplace=True)
    for index, person in queue.iterrows():
        total += person.weight
        if total > 1000:
            return pd.DataFrame({'person_name':[result]})
        result = person.person_name
    return pd.DataFrame({'person_name':[result]})

# Pandas solution:
def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn', inplace=True)
    queue['weight'] = queue.weight.cumsum()
    return queue[queue.weight <= 1000].tail(1)[['person_name']]