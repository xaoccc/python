participants = input().split(", ")
songs = input().split(", ")
collection = {}

command = input()
while command != "dawn":
    command = command.split(", ")
    if command[0] in participants and command[1] in songs:
        if command[0] not in collection.keys():
            collection[command[0]] = {command[1] : [command[2]]}
            
        elif command[0] in collection:
            if command[1] not in collection[command[0]].keys():
                collection[command[0]][command[1]] = [command[2]]
                
            elif command[2] not in collection[command[0]][command[1]]:
                collection[command[0]][command[1]].append(command[2])
            

    command = input()
for performer, music in collection.items():
    print(f"{performer}: ", end="")
    for song, awards in music.items():
         print(f"{len(awards)} awards")
         for award in awards:
            print(f"--{award}")
