from math import floor
record_sec = float(input())
distance_m = float(input())
time_per_m = float(input())
 
total_time = (distance_m * time_per_m) + ((floor(distance_m / 50)) * 30)
if total_time < record_sec:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time-record_sec:.2f} seconds slower.")
