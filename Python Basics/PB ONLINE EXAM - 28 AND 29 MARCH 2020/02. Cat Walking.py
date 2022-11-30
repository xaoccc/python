walk_min = int(input())
walk_num = int(input())
cal_day = int(input())
 
total_walk_min = walk_num * walk_min
cal_burned = total_walk_min * 5
if (cal_day / 2) <= cal_burned:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {cal_burned}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {cal_burned}.")
