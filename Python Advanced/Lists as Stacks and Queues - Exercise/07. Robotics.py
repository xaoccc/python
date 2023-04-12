import datetime
from datetime import timedelta

robots = input().split(";")
robots_data = {}
robots_ready = {}
robots_database = {}
for robot in robots:
    robot = robot.split("-")
    robots_data[robot[0]] = int(robot[1])
    robots_database[robot[0]] = int(robot[1])
    
start_time = [int(i) for i in input().split(":")]
new_time = datetime.datetime(2000,7,7,start_time[0], start_time[1], start_time[2])
command = input()
while command != "End":
    new_time += timedelta(seconds=1)
    print_time = new_time.strftime("%H:%M:%S")
    for robot, time in robots_data.items():
        if sum(robots_data.values()) == 0:
            new_time = min(robots_ready.values())
            print(f"{robots_ready[robot]} - {command} [{robots_ready.values()}]")
        
        elif time > 0:
            print(f"{robot} - {command} [{print_time}]")
            ready = new_time+timedelta(seconds=time)
            print(f"Will be available again at {ready.strftime('%H:%M:%S')}")
            robots_ready[robot] = ready.strftime('%H:%M:%S')
            robots_data[robot] = 0
            break

        
    print(robots_ready)
    for robot, time in robots_ready.items():
        if print_time == time:
            robots_data[robot] = robots_database[robot]
    
    command = input()
