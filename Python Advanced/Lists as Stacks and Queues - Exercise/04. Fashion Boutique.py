clothes = [int(i) for i in input().split()]
rack_capacity = int(input())
racks_needed = 0
current_sum = 0
for i in range(len(clothes)-1, -1, -1):
    current_sum += clothes[i]
    if current_sum == rack_capacity:
        racks_needed += 1
        current_sum = 0
    if current_sum > rack_capacity:
        racks_needed += 1
        current_sum = clothes[i]
if current_sum > 0:
    racks_needed += 1
print(racks_needed)
