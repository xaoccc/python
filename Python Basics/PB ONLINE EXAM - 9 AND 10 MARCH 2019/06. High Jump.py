end_height = int(input())
start_height = end_height - 30
 
jumps_counter = 0
fails = 0
 
for current_height in range(start_height, end_height + 1, 5):
    for i in range(1, 3 + 1):
        jump = int(input())
        jumps_counter += 1
 
        if jump > current_height:
            fails = 0
            break
        else:
            fails += 1
            if fails >= 3:
                print(f"Tihomir failed at {current_height}cm after {jumps_counter} jumps.")
                raise SystemExit
 
print(f"Tihomir succeeded, he jumped over {current_height}cm after {jumps_counter} jumps.")
