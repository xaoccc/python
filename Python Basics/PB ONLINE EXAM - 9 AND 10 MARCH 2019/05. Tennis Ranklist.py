#user input
tournaments_num = int(input())
initial_points = int(input())
points_sum = 0
wins_n = 0
from math import floor
 
#logic
#checking each tournament
for i in range (0, tournaments_num) :
    place = input()
#counting the number of wins and summing points in the variable points_sum
    if place == "W" :
        wins_n += 1
        points_sum += 2000
    elif place == "F" :
        points_sum += 1200
    elif place == "SF" :
        points_sum += 720
 
points_total = initial_points + points_sum
points_avg = points_sum / tournaments_num
wins = wins_n * 100 / tournaments_num
 
#print output
print(f"Final points: {points_total}")
print(f"Average points: {floor(points_avg)}")
print(f"{wins:.2f}%")
