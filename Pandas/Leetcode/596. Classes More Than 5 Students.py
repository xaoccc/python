import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counts = courses['class'].value_counts().reset_index()
    return counts.loc[(counts['count'] >= 5),['class']]