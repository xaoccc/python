import pandas as pd
data = {
    'actor_id': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Charlie', 'Alice', 'Charlie', 'Bob', 'Bob', 'Charlie', 'Bob'],
    'director_id': ['XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'XYZ', 'ABC', 'ABC'],
    'director_age': [45, 50, 45, 50, 45, 50, 45, 50, 45, 45, 50, 50]
}
df = pd.DataFrame(data)
def test(data):

    result = data.groupby('director_id').sum()


    return result
print(test(df))