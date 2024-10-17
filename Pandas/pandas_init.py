import pandas as pd
data = {
    'actor_id': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Charlie', 'Alice', 'Charlie', 'Bob', 'Bob', 'Charlie', 'Bob'],
    'director_id': ['XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'ABC', 'XYZ', 'XYZ', 'ABC', 'ABC']
}

actor_director = pd.DataFrame(data)

df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)],
                  columns=['dogs', 'cats'])
print(df.round({'dogs': 0, 'cats': 4}))