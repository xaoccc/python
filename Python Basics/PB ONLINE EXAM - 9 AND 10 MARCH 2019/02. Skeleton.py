control_min = int(input())
control_sec = int(input())
u_length = float(input())
sec_per_100m = int(input())
time = (u_length / 100) * sec_per_100m
time_less = (u_length / 120) * 2.5
total_time = time - time_less
control_time = (control_min * 60) + control_sec
if control_time >= total_time :
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {total_time - control_time:.3f} second slower.")
