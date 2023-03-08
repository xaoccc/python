tracks_num = int(input())
tracks_dict = {}
for num in range(tracks_num):
    tracks_list = input().split("|")
    piece = tracks_list[0]
    composer = tracks_list[1]
    key = tracks_list[2]
    tracks_dict[piece] = [composer, key]
   
command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        if command[1] in tracks_dict.keys():
            print(f"{command[1]} is already in the collection!")
        else:
            tracks_dict[command[1]] = [command[2], command[3]]
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
    elif command[0] == "Remove":
        if command[1] in tracks_dict.keys():
            del tracks_dict[command[1]]
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        if command[1] in tracks_dict.keys():
            tracks_dict[command[1]] = [tracks_dict[command[1]][0], command[2]]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    

    command = input()
for (key, value) in tracks_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
