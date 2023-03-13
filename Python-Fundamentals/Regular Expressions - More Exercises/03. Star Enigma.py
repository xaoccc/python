import re
message_num = int(input())
decode_data = ["s", "t", "a", "r", "S", "T", "A", "R"]
attacked, destroyed = [], []

#for each compile group/name we add starting chars equal to the sum of all starting chars @!:-> Logic is that after each group we have next group.
planet = re.compile(
    r"@(?P<planet>[a-zA-Z]+)([^\@\-\!\:\>]*)" 
    r":(?P<population>[0-9]+)([^\@\-\!\:\>]*)" 
    r"(\!)(?P<attack>[A,D])!([^\@\-\!\:\>]*)"
    r"->(?P<army>[0-9]+)")

for i in range(message_num):
    decode_chars = 0
    decoded_message = ""
    message = input()
    for char in message:
        if char in decode_data:
            decode_chars += 1
    for char in message:
        decoded_message += chr(ord(char) - decode_chars)
    result = re.finditer(planet, decoded_message)
    
    for show in result:
        if show["attack"] == "A":
            attacked.append(show["planet"])
        elif show["attack"] == "D":
            destroyed.append(show["planet"])
            
attacked, destroyed = sorted(attacked), sorted(destroyed)
       
print(f"Attacked planets: {len(attacked)}")
for i in attacked:
    print(f"-> {i}")
print(f"Destroyed planets: {len(destroyed)}")
for i in destroyed:
    print(f"-> {i}")
