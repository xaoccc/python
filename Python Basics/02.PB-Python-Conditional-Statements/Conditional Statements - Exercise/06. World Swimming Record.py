world_record = float(input())
dist = float(input())
speed = float(input())
time = (dist * speed) + (dist // 15) * 12.5
if time < world_record :
    print (f" Yes, he succeeded! The new world record is {time:.2f} seconds.")
else :
    print (f"No, he failed! He was {(time - world_record):.2f} seconds slower.")
