from collections import deque
males, females = deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()])
matches = 0

def remove_gender(gender, idx):
    if gender[idx] <= 0 or gender[idx] % 25 == 0:
        if gender[idx] > 0:
            del gender[idx]
        del gender[idx]
        return True
    return False

while males and females:
    if remove_gender(males, -1) or remove_gender(females, 0):
        continue
    male, female = males.pop(), females.popleft()
    if male == female:
        matches += 1
    else:
        males.append(male - 2)
    
print(f"Matches: {matches}\nMales left: ", end="")
if not males:
    print("none\nFemales left: ", end="")
else:

    print(f"{', '.join([str(i) for i in list(reversed(males))])}\nFemales left: ", end="")
if not females:
    print("none")
else:
    print(f"{', '.join([str(i) for i in females])}")

# from collections import deque
# males, females = deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()])
# matches = 0
# while males and females:
    
#     if males[-1] <= 0 or males[-1] % 25 == 0:
#         if males[-1] > 0:
#             males.pop()
#         males.pop()
#         continue
#     if females[0] <= 0 or females[0] % 25 == 0:
#         if females[0] > 0:
#             females.popleft()
#         females.popleft()
#         continue

#     male = males.pop()
#     female = females.popleft()
#     if male == female:
#         matches += 1
#     else:
#         males.append(male - 2)

# print(f"Matches: {matches}\nMales left: ", end="")
# if not males:
#     print("none\nFemales left: ", end="")
# else:
#     print(f"{', '.join([str(i) for i in list(reversed(males))])}\nFemales left: ", end="")
# if not females:
#     print("none")
# else:
#     print(f"{', '.join([str(i) for i in females])}")
