from collections import deque

green_light = int(input())
free_window = int(input())
traffic_data = deque()
command = input()
while command != "END":
    traffic_data.append(command)
    command = input()