command = input()
all_users = {}


while command != "Lumpawaroo":
    if " | " in command:
        command = command.split(" | ")
        force_user = command[1]
        force_side = command[0]
        if force_side not in all_users:
            all_users[force_side] = []
            if force_user not in all_users.values():
                all_users[force_side].append(force_user)

    else:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        if force_side not in all_users.keys():
            all_users[force_side] = []

        for (key, value) in all_users.items():
            if force_user in value:
                value.remove(force_user)
        all_users[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for (key, value) in all_users.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in value:
            print(f"! {i}")
