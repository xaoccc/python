from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(reversed([int(i) for i in input().split()]))
locks = deque(int(i) for i in input().split())
budget = int(input())
total_bullets = len(bullets)

while locks:
    if gun_barrel_size > len(bullets):
        gun_barrel_size = len(bullets)
    for i in range(gun_barrel_size):
        if bullets[i] <= locks[0]:
            print("Bang!")
            locks.popleft()
        elif bullets[i] > locks[0]:
            print("Ping!")
            locks.appendleft(locks.popleft())
        elif len(bullets) == 0:
            break
        
    bullets = bullets[gun_barrel_size: ]
    if bullets:
        print("Reloading!")
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${budget - (bullet_price * (total_bullets - len(bullets)))}")
        break
    elif not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
