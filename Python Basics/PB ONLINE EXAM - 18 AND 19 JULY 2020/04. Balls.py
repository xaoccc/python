from math import floor
balls_num = int(input())
red_num = 0
orange_num = 0
yellow_num = 0
white_num = 0
black_num = 0
others_num = 0
pts = 0
 
for i in range(balls_num):
    ball_colour = input()
    if ball_colour == "red":
        red_num += 1
        pts += 5
    elif ball_colour == "orange":
        orange_num += 1
        pts += 10
    elif ball_colour == "yellow":
        yellow_num += 1
        pts += 15
    elif ball_colour == "white":
        white_num += 1
        pts += 20
    elif ball_colour == "black":
        black_num += 1
        pts = floor(pts / 2)
    else:
        others_num += 1
        continue
print(f"Total points: {pts}")
print(f"Red balls: {red_num}")
print(f"Orange balls: {orange_num}")
print(f"Yellow balls: {yellow_num}")
print(f"White balls: {white_num}")
print(f"Other colors picked: {others_num}")
print(f"Divides from black balls: {black_num}")
