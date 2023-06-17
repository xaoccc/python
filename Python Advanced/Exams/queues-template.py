from collections import deque
deque_one, deque_two = deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()])

while deque_one and deque_two:
  current_deque_one = deque_one.pop()/deque_one.popleft()
  current_deque_two = deque_two.pop()/deque_two.popleft()
  #logic...

if deque_one:
  print(f"Some text {''.join([str(i) for i in deque_one])}")
if deque_two:
  print(f"Some text {''.join([str(i) for i in deque_two])}")
