#user input
n = int(input())
daynight = input()
taxi_entry = 0.7
taxi_day_rate = 0.79
taxi_night_rate = 0.9
bus_rate = 0.09
train_rate = 0.06

#logic

if n >= 100 :
    rate = n * train_rate
elif n >= 20 :
    rate = n * bus_rate
elif n < 20 :
    if daynight == "day" :
        rate = taxi_entry + n * taxi_day_rate
    elif daynight == "night" :
        rate = taxi_entry + n * taxi_night_rate

#output
print(f"{rate:.2f}")