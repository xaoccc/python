days = int(input())
hours = int(input())
parking_sum_day = 0
parking_sum_total = 0

for i in range(1, days + 1):
    parking_sum_day = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            parking_sum_day += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            parking_sum_day += 1.25
        else:
            parking_sum_day += 1
        if j == hours:
            print(f"Day: {i} - {parking_sum_day:.2f} leva")
    parking_sum_total += parking_sum_day

print(f"Total: {parking_sum_total:.2f} leva")