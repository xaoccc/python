days = int(input())
daily_plunder = int(input())
expected_plunder  = int(input())
total_plunder = 0
current_plunder = daily_plunder

for day in range(1, days + 1):
    daily_plunder = current_plunder
    if day % 3 == 0:
        daily_plunder *= 1.5

    total_plunder += daily_plunder
    if day % 5 == 0:
        total_plunder *= 0.7
    
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder / expected_plunder * 100:.2f}% of the plunder.")
