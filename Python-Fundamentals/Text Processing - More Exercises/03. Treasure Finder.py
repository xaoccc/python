import re
key = input().split()
command = input()

while command != "find":
    output = ""
    #We need to have a key with length >= command length. This is one way to do it :)
    new_key = key * (len(command) // len(key) + 1)
    
    #for each command character, we decode using the key:
    for i in range(len(command)):
        output += chr(ord(command[i]) - int(new_key[i]))
        
    #We are looking for human words, so we can simply use regex findall and \w+ for alphabetical characters after "&", we need just the first one, so we write [0] and we do not want to have "&", so we skip it [1: ]
    treasure_type = re.findall(r'&\w+', output)[0][1: ]
    
    #Do the same for the coordinates, using "<", instead of "&"
    coordinates = re.findall(r'<\w+', output)[0][1: ]
    
    #Print the result for each treasure found:
    print(f"Found {treasure_type} at {coordinates}")
    command = input()
