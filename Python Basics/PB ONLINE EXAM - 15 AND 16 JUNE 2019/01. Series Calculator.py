from math import ceil
movie = input()
seasons = int(input())
series = int(input())
s_length = float(input())

ads_length = s_length * 0.2
total_s_length = s_length * series * seasons
total_ads_length = ads_length * series * seasons
spec_s_length = seasons * 10
time_total = total_s_length + total_ads_length + spec_s_length

print(f"Total time needed to watch the {movie} series is {ceil(time_total)} minutes.")
