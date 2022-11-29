import math
sname = input()
slength = int(input())
brlength = int(input())

lunch = brlength * 0.125
rest = brlength * 0.25

if slength > brlength - (lunch + rest) :
    print (f"You don't have enough time to watch {sname}, you need {math.ceil(slength - (brlength - (lunch + rest)))} more minutes.")
else :
    print (f"You have enough time to watch {sname} and left with {math.ceil((brlength - (lunch + rest) - slength))} minutes free time.")
