from collections import deque
stack = deque()
actions_num = int(input())

for i in range(actions_num):
    command = input()
    if command[0] == "1":
        stack.appendleft(int(command.split()[1]))
    elif command == "2":
        if len(stack) > 0:
            stack.popleft()
    elif command == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command == "4":
        if len(stack) > 0:
            print(min(stack))
stack = ", ".join([str(i) for i in stack])
print(stack)
