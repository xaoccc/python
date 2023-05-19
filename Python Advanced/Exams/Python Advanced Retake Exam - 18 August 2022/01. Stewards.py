from collections import deque
seats, first_nums, second_nums = input().split(", "), deque(input().split(", ")), deque(input().split(", "))
seat_matches = []
rotations = 0

while first_nums and second_nums:
    first_num = first_nums.popleft()
    second_num = second_nums.pop()
    char = chr(int(first_num) + int(second_num))
    if first_num + char in seats:
        seat_matches.append(first_num + char)
        seats.remove(first_num + char)

    if second_num + char in seats:
        seat_matches.append(second_num + char)
        seats.remove(second_num + char)

    if (first_num + char not in seats) and (second_num + char not in seats) and (first_num + char not in seat_matches) and (second_num + char not in seat_matches):
        first_nums.append(first_num)
        second_nums.appendleft(second_num)
    rotations += 1
    if rotations == 10 or len(seat_matches) == 3:
        break

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
