records = int(input())
all_cars = []

for i in range(records):
    car = tuple(map(str, input().split(", ")))
    if car[0] == "IN":
        all_cars.append(car[1])
    elif car[0] == "OUT": 
        if car[1] in all_cars:
            all_cars.remove(car[1])
if all_cars:
    print(*set(all_cars), sep="\n")
else:
    print("Parking Lot is Empty")
