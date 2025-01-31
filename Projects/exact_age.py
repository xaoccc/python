import datetime as dt

birth_date = [int(num) for num in input('Enter your birth date in the format YYYY-MM-DD: ').split('-')]
time_now = dt.datetime.now()
some_date = dt.datetime(birth_date[0],birth_date[1],birth_date[2])

print(f'You are {(time_now - some_date).days//365} years, {(time_now - some_date).days%365//30} months, {(time_now - some_date).days%365%30} days, {time_now.hour - some_date.hour} hours, {time_now.minute - some_date.minute} minutes, {  time_now.second - some_date.second} seconds old.')  
