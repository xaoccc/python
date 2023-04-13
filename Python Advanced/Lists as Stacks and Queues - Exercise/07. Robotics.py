import datetime
from datetime import timedelta

def get_key(val):
    for key, value in robots_ready.items():
        if val == value:
            return key

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
    for robot, time in robots_data.items():
        
        if sum(robots_data.values()) == 0:
            new_time = min(robots_ready.values())
            print(f"{get_key(min(robots_ready.values()))} - {command} [{min(robots_ready.values()).strftime('%H:%M:%S')}]")
            ready = new_time+timedelta(seconds=robots_database[robot])
            robots_ready[robot] = ready
            break
        
        elif time > 0:
            print(f"{robot} - {command} [{new_time.strftime('%H:%M:%S')}]")
            ready = new_time+timedelta(seconds=time)
            robots_ready[robot] = ready
            robots_data[robot] = 0
            break

    for robot, time in robots_ready.items():
        if new_time.strftime('%H:%M:%S') == time:
            robots_data[robot] = robots_database[robot]
    
    command = input()
