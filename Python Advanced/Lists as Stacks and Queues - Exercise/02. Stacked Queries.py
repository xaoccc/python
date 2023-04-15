from collections import deque
numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else print(),
    4: lambda x: print(min(numbers)) if numbers else print()
}

for i in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)
numbers.reverse()
print(*numbers, sep=", ")



# stack = deque()
# actions_num = int(input())
#
# for i in range(actions_num):
#     command = input()
#     if command[0] == "1":
#         stack.appendleft(int(command.split()[1]))
#     elif command == "2":
#         if len(stack) > 0:
#             stack.popleft()
#     elif command == "3":
#         if len(stack) > 0:
#             print(max(stack))
#     elif command == "4":
#         if len(stack) > 0:
#             print(min(stack))
# stack = ", ".join([str(i) for i in stack])
# print(stack)
