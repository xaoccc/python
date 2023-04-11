from collections import deque
queue = deque()
quantity = int(input())
name = input()
while name != "Start":
    queue.append(name)
    name = input()
    
command = input()    
while command != "End":
    if command.isdigit():
        if quantity >= int(command):
            quantity -= int(command)
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    else:
        quantity += int(command.split()[1])
    command = input() 
print(f"{quantity} liters left")
