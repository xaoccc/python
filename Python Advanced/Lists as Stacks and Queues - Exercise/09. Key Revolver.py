from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(i) for i in input().split()]
locks = deque(int(i) for i in input().split())
budget = int(input())
total_bullets = len(bullets)

while locks:
    if gun_barrel_size > len(bullets):
        gun_barrel_size = len(bullets)
    for i in range(gun_barrel_size):
        if bullets[-1] <= locks[0]:
            print("Bang!")
            locks.popleft()
            if len(locks) == 0:
                bullets.pop()
                break
        elif bullets[-1] > locks[0]:
            print("Ping!")
            locks.appendleft(locks.popleft())
        elif len(bullets) == 0:
            break
        bullets.pop()
        
    if bullets and i == (gun_barrel_size - 1):
        print("Reloading!")
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${budget - (bullet_price * (total_bullets - len(bullets)))}")
        break
    elif not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
