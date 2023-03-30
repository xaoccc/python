command = input()
log = {}


while command != "end":
    command = command.replace("IP=", "")
    command = command.replace("message=", "")
    command = command.replace("user=", "")
    command = command.split()
    user_name = command[2]
    ip = command[0]
    if user_name not in log.keys():
        log[user_name] = {ip: 1}
    else:
        if ip not in log[user_name].keys():
            log[user_name][ip] = 1
        else:
            log[user_name][ip] += 1
    
    command = input()

log = dict(sorted(log.items(), key=lambda x: x[0]))


for user, conn in log.items():
    current_result = []
    print(f"{user}: ")
    for ip_num, visit_num in conn.items():
        current_result.append(f"{ip_num} => {visit_num}")
    print(*current_result, sep=", ", end=".\n")
