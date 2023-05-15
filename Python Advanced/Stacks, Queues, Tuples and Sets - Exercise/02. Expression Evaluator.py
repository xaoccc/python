#
# expression = [int(i) if i.isnumeric() or i.lstrip("-").isdigit() else i for i in input().split()]
# current = []
# result = 0
# for i in range(len(expression)):
#     if type(expression[i]) == int:
#         current.append(expression[i])
#     else:
#         if expression[i] == "-":
#             result = current[0]
#             for num in range(1, len(current)):
#                 result -= current[num]
#             current = [result]
#         elif expression[i] == "+":
#             result = current[0]
#             for num in range(1, len(current)):
#                 result += current[num]
#             current = [result]
#         elif expression[i] == "*":
#             result = current[0]
#             for num in range(1, len(current)):
#                 result *= current[num]
#             current = [result]
#         elif expression[i] == "/":
#             result = current[0]
#             for num in range(1, len(current)):
#                 result //= current[num]
#             current = [result]
#
# print(result)

from collections import deque
from math import floor
expression = deque(input().split())
idx = 0

while idx < len(expression):
    element = expression[idx]
    if element in "-+/*":
        for i in range(idx - 1):
            expression.appendleft(eval(f"{int(expression.popleft())} {element} {int(expression.popleft())}"))
        del expression[1]
        idx = 1
    idx += 1

print(floor(int(expression[0])))
