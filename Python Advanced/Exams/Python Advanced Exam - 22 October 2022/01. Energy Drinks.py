from collections import deque
stamat_caffeine = 0
caffeine, redbull = deque([int(i) for i in input().split(", ")]), deque([int(i) for i in input().split(", ")])
while caffeine and redbull:
    current_caffeine = caffeine.pop()
    current_energy = redbull.popleft()
    if stamat_caffeine + (current_caffeine * current_energy) <= 300:
        stamat_caffeine += current_caffeine * current_energy
    else:
        redbull.append(current_energy)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0

if redbull:
    print(f"Drinks left: {', '.join([str(i) for i in redbull])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
