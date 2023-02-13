start_time = [int(i) for i in input().split(":")]
steps = int(input())
speed = int(input())
walk_seconds = steps * speed
start_time_seconds = start_time[2] + start_time[1] * 60 + start_time[0] * 3600
total_seconds = start_time_seconds + walk_seconds

hours = total_seconds // 60 // 60 % 24
minutes = total_seconds // 60 % 60
seconds = total_seconds % 60

print(f"Time Arrival: {hours:02d}:{minutes:02d}:{seconds:02d}")
