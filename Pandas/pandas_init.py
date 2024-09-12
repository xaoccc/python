import pandas as pd
dates = pd.date_range('2015-01-15', periods=2)
weather = pd.DataFrame({'id': list('12'), 'recordDate': ['2015-01-16', '2015-01-14'], 'temperature': [3,-1]})
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate', ascending=True)
    return weather.loc[(weather['temperature'] > weather['temperature'].shift(1)) & (pd.to_datetime(weather['recordDate']) == pd.to_datetime(weather['recordDate'].shift(1)) + pd.Timedelta(days=1) ), ['id']]



