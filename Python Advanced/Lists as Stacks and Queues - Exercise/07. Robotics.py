# SUPER HARD TASK!!!! Using complex comprehensions, datetime methods, dictionaries, nested lists, queues and loops
from collections import deque
from datetime import datetime, timedelta

# User inputs
# create a dictionary from the input:
# input().split(";") divides the input into different robots, for each robot, we split into "-"
# and take the key(str) and the value(list, consisting of 2 int)
# The key is the robot name, values are total time for completing the task and the time used for current task
robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}
# .strptime() method (literally string parse time) takes 2 arguments - 1 string to parse into datetime format and
# the actual format we need (DD:MM, YYYY-MM-DD or HH:MM:SS) the last one we heed here
# Remember, to print we need to use strftime() to display it. Here we use it just for calculation purposes
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()
# Add all products in a queue
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

# Logic
while products:
    # Our step is 1 second, so we move 1 second forward in every loop (in timedelta 0 is for days, 1 is for seconds)
    factory_time += timedelta(0, 1)
    # remove the product from the assembly line tasks, as first we assume it is being produced
    product = products.popleft()

    # Decrease the time left until free again for all robots that are in production mode (else do not decrease)
    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    # Check for idle robots (if any)
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    # Still if there is no free robot to make this product, we add it to the end of the product line (queue)
    if not free_robots:
        products.append(product)
        continue

    # If there is a free robot (free_robots[0]), we can give him a task
    # To do this, we place the total time for completing the task on the time used for current task
    # And if you return on line 28, you'll see we'll decrease it later until it hits zero
    robots[free_robots[0][0]][1] = free_robots[0][1][0]
    # Output
    # free_robots[0][0] is the robot name working on the current product
    # .strftime() method converts time format from YYYY-MM-DD HH:MM:SS to the desired one very easily
    # strftime literally means "string format time" and takes 1 argument
    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")




# My try for solving the problem 33/100:
# import datetime
# from datetime import timedelta
#
# def get_key(val):
#     for key, value in robots_ready.items():
#         if val == value:
#             return key
#
# robots = input().split(";")
# robots_data = {}
# robots_ready = {}
# robots_database = {}
# for robot in robots:
#     robot = robot.split("-")
#     robots_data[robot[0]] = int(robot[1])
#     robots_database[robot[0]] = int(robot[1])
#
# start_time = [int(i) for i in input().split(":")]
# new_time = datetime.datetime(2000,7,7,start_time[0], start_time[1], start_time[2])
# command = input()
# while command != "End":
#     new_time += timedelta(seconds=1)
#     for robot, time in robots_data.items():
#
#         if sum(robots_data.values()) == 0:
#             new_time = min(robots_ready.values())
#             print(f"{get_key(min(robots_ready.values()))} - {command} [{min(robots_ready.values()).strftime('%H:%M:%S')}]")
#             ready = new_time+timedelta(seconds=robots_database[robot])
#             robots_ready[robot] = ready
#             break
#
#         elif time > 0:
#             print(f"{robot} - {command} [{new_time.strftime('%H:%M:%S')}]")
#             ready = new_time+timedelta(seconds=time)
#             robots_ready[robot] = ready
#             robots_data[robot] = 0
#             break
#
#     for robot, time in robots_ready.items():
#         if new_time.strftime('%H:%M:%S') == time:
#             robots_data[robot] = robots_database[robot]
#
#     command = input()
