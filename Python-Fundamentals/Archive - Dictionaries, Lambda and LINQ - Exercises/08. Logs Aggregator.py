logs_num = int(input())
all_data = {}

for i in range(logs_num):
    log = input().split()
    ip = log[0]
    user = log[1]
    duration = int(log[2])
    if user not in all_data.keys():
        all_data[user] = {ip: duration}
    else:
        if ip not in all_data[user].keys():
            all_data[user][ip] = duration
        else:
            all_data[user][ip] += duration

all_data = dict(sorted(all_data.items(), key=lambda x: x[0]))

for user in all_data:
    all_data[user] = dict(sorted(all_data[user].items(), key=lambda x: x[0]))

for user, data in all_data.items():
    current_data = list(data.keys())
    print(f"{user}: {sum(data.values())} [", end="")
    for i in range(len(current_data)):
        if i != len(current_data) - 1:
            print(f"{current_data[i]}", end=", " )
        else:
            print(f"{current_data[i]}", end="" )
    print("]")
