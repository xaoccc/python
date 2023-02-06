couples = [int(i) for i in input().split("@")]
command = input()

while command != "Love!":
    command = command.split()
    if command[0] == "Jump":
