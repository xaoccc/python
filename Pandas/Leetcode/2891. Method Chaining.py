import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.sort_values('weight', ascending=False).loc[animals['weight'] > 100, ['name']]