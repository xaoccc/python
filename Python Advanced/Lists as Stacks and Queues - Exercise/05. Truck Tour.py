# SUPER HARD PROBLEM!!!!!!!!!!!!!!!

from collections import deque

fuel_distance = deque()
petrol_pumps = int(input())

# We should add all petrol stations into a queue, so we can check which would be the first possible
for i in range(petrol_pumps):
    command = [int(i) for i in input().split()]
    fuel_distance.append([command[0], command[1]])

# We make a copy of the queue, so we can make our loop work correctly
fuel_distance_copy = fuel_distance.copy()
# We need 2 variables - pump_idx - the result and gas_in_tank - the current available fuel
pump_idx, gas_in_tank = 0, 0

# If we use the original queue fuel_distance, we would have an infinite loop
# So we use the copy
while fuel_distance_copy:
    # We assume the petrol is enough and remove the data from the copy queue
    petrol, distance = fuel_distance_copy.popleft()
    # And we add the fuel in the tank, because we always do this, according to the problem description
    gas_in_tank += petrol
    # But if the current available fuel is not enough to get to the next gas station,
    # we rotate the original queue and use it for the copy
    # The gas becomes 0 and the index of the gas station increases by one
    if gas_in_tank < distance:
        fuel_distance.rotate(-1)
        fuel_distance_copy = fuel_distance.copy()
        pump_idx += 1
        gas_in_tank = 0
    # If we have enough fuel to the next gas station, we must not forget to remove the used fuel on the road between
    # The two stations
    else:
        gas_in_tank -= distance

print(pump_idx)


