rooms_num = int(input())
free_chairs_num = 0
free_chairs = -1

for room in range(1, rooms_num +1):
    chairs_num = input().split()
    if len(chairs_num[0]) < int(chairs_num[1]):
        free_chairs = 0
        print(f"{int(chairs_num[1]) - len(chairs_num[0])} more chairs needed in room {room}")
    else:
        free_chairs_num += len(chairs_num[0]) - int(chairs_num[1])
if free_chairs != 0:
    print(f"Game On, {free_chairs_num} free chairs left")
