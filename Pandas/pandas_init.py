import pandas as pd
import numpy as np


dates = pd.date_range('20240505', periods=10)


# df = pd.DataFrame(np.random.randn(10, 6), index=dates, columns=list('ABCDEF'))
df = pd.read_csv('csv_data.csv')
df = df.loc[df.Maxpulse.duplicated(), :]


print(df)

