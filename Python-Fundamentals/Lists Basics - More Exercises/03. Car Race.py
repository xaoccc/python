nums = input()
car_two, car_one = nums.split(" "), nums.split(" ")
del car_two[0 : (len(car_two) // 2) + 1]
del car_one[(len(car_one) // 2) : len(car_one) + 1]
car_one_sum_time = 0
car_two_sum_time = 0

for i in range(len(car_one)):
    car_one[i] = int(car_one[i])
    car_one_sum_time += car_one[i]
    if car_one[i] == 0:
        car_one_sum_time *= 0.8

for j in range(len(car_two) - 1, -1, -1):       
    car_two[j] = int(car_two[j])    
    car_two_sum_time += car_two[j]
    if car_two[j] == 0:
        car_two_sum_time *= 0.8
    
    
if car_one_sum_time < car_two_sum_time:
    print(f"The winner is left with total time: {car_one_sum_time:.1f}")
else:
    print(f"The winner is right with total time: {car_two_sum_time:.1f}")
