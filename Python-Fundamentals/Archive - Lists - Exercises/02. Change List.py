nums = input().split()
command = input()

while command != "Odd" and command != "Even":
    command = command.split()
    if command[0] == "Delete":
        nums = list(filter((command[1]).__ne__, nums))
    elif command[0] == "Insert":
        nums.insert(int(command[2]), command[1])
    command = input()
    
if command == "Odd":
    result = [int(i) for i in nums if int(i) % 2 != 0]
elif command == "Even":
    result = [int(i) for i in nums if int(i) % 2 == 0]
    
print(*result)
