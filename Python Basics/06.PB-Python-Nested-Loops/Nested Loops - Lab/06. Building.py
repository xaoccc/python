floors_total = int(input())
apts_floor = int(input())
apt_name = ""

for floor in range(floors_total, 0, -1):
    for apt in range(0, apts_floor):
        if floor == floors_total:
            print("L{floor}{apt} ", end = "")
        continue
        if floor % 2 == 0:
            print("O{floor}{apt} ", end = "")
        else:
            print("A{floor}{apt} ", end = "")
    print("")