usernames = input().split(" ")
result = 0

for j in range(min(len(usernames[0]), len(usernames[1]))):
    result += ord(usernames[0][j]) * ord(usernames[1][j])
if len(usernames[0]) > len(usernames[1]):
    for i in range(len(usernames[1]), len(usernames[0])):
        result += ord(usernames[0][i])
elif len(usernames[0]) < len(usernames[1]):
    for i in range(len(usernames[0]), len(usernames[1])):
        result += ord(usernames[1][i])

print(result)