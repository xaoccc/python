users_num = int(input())
all_users = []
for i in range(users_num):
    all_users.append(input())
print(*set(all_users), sep="\n")
