couples = [int(i) for i in input().split("@")]
command = input()
jump = 0

while command != "Love!":
    command = command.split()
    love_index = int(command[1]) + jump

    if command[0] == "Jump":
        if love_index >= len(couples):
            love_index = 0
        if couples[love_index] == 0:
            print(f"Place {love_index} already had Valentine's day.")
        else:
            couples[love_index] -= 2
            if couples[love_index] == 0:
                print(f"Place {love_index} has Valentine's day.")
    jump = love_index
    command = input()

print(f"Cupid's last position was {love_index}.")
if sum(couples) == 0:
    print("Mission was successful.")
else:
    fail_count = len(list(filter(lambda x: (x > 0), couples)))
    print(f"Cupid has failed {fail_count} places.")
