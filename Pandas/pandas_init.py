import pandas as pd
data = {
    'actor_id': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Charlie', 'Alice', 'Charlie', 'Bob', 'Bob', 'Charlie', 'Bob'],
    'director_id': ['XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'XYZ', 'ABC', 'ABC']
}

actor_director = pd.DataFrame(data)

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # 1. We group the data from combined columns 'actor_id' and 'director_id'
    grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts').query('counts > 2')
    print(grouped)

    grouped_count = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()
    print(grouped_count)

    return grouped.loc[grouped['counts'] > 2, ['actor_id', 'director_id']]


actors_and_directors(actor_director)