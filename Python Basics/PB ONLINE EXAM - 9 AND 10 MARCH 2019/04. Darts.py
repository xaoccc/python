player = input()
total_pts = 301
area = ""
succ_shots = 0
unsucc_shots = 0
while area != "Retire":
    area = input()
    if area == "Retire":
        print(f"{player} retired after {unsucc_shots} unsuccessful shots.")
        break
    pts = int(input())
    if area == "Double":
        pts *= 2
    elif area == "Triple":
        pts *= 3
    if total_pts >= pts:
        total_pts -= pts
        succ_shots += 1
    else:
        unsucc_shots += 1
    if total_pts == 0:
        print(f"{player} won the leg with {succ_shots} shots.")
        break
