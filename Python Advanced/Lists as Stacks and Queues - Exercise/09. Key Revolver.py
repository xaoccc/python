from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(i) for i in input().split()]
bullets = list(reversed(bullets))
locks = deque(int(i) for i in input().split())
budget = int(input())
total_bullets = len(bullets)


while locks:
    for i in range(gun_barrel_size):
        if bullets[i] <= locks[0]:
            print("Bang!")
            locks.popleft()
        else:
            print("Ping!")
            locks.appendleft(locks.popleft())

        if len(bullets) == 0:
            print(f"Couldn't get through. Locks left: {len(locks)}")
            break
    bullets = bullets[gun_barrel_size: ]
    if gun_barrel_size > len(bullets) and len(bullets) != 0:
        gun_barrel_size = len(bullets)
    if len(bullets) > 0:
        print("Reloading!")
    if len(locks) == 0:
        print(f"{len(bullets)} bullets left. Earned ${budget - (bullet_price * (total_bullets - len(bullets)))}")
        break
    elif len(bullets) == 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
