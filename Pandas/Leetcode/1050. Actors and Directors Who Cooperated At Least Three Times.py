import pandas as pd

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # 1. We take the combination of columns 'actor_id' and 'director_id' using groupby()
    # 2. We count the occurrences of each combination using size()
    # 3. Use a column to store each result: reset_index(name='counts') and filter only unique values of combinations
    # 4. Get only the values of counts column greater than 2: query('counts > 2')
    # 5. Display the selected columns from the df: [['actor_id', 'director_id']]
    return actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts').query('counts > 2')[['actor_id', 'director_id']]

