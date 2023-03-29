command = input()
log = {}


while command != "end":
    command = command.replace("IP=", "")
    command = command.replace("message=", "")
    command = command.replace("user=", "")
    command = command.split()
    if command[0] not in log.keys():
        command = input()



# log = dict(sorted(log.items(), key=lambda x: x[0]))
# for user, conn in log.items():
#     print(f"{user}: ")
#     for ip_num, visit_num in conn.items():
#         print(f"{ip_num} => {visit_num}.")