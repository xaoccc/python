from collections import deque
tj = deque(input().split(", "))

turn = 0
area_map = []
rest = False
both_rest = False

for row in range(6):
    area_map.append(input().split())

while True:
    coordinates = [int(i) for i in input()[1:-1].split(", ")]
    if both_rest == True:
        both_rest = False
        continue

    if area_map[coordinates[0]][coordinates[1]] == "W":
        print(f"{tj[turn]} hits a wall and needs to rest.")
        if rest == True:
            both_rest = True
            rest = False
            continue
        rest = True
        

    elif area_map[coordinates[0]][coordinates[1]] == "T":
        print(f"{tj[turn]} is out of the game! The winner is {tj[turn - 1]}." )
        break
    elif area_map[coordinates[0]][coordinates[1]] == "E":
        print(f"{tj[turn]} found the Exit and wins the game!")
        break

    turn += 1
    if turn == 2:
        turn = 0

        
        
# from collections import deque
# tj = input().split(", ")
# tj_copy = tj.copy()

# turn = 0
# area_map = []
# skip_tom, skip_jerry = 0, 0
# tom_rest, jerry_rest = False, False
# winner = ""

# for row in range(6):
#     area_map.append(input().split())

# while True:
#     coordinates = [int(i) for i in input()[1:-1].split(", ")]
    
#     if tom_rest:
#         skip_tom += 1
#         if skip_tom == 3:
#             skip_tom = 0
#             tom_rest = False
#             tj.append("Tom")
#             if len(tj) == 2 and tj != tj_copy:
#                 tj = tj_copy.copy()

#     if jerry_rest:
#         skip_jerry += 1
#         if skip_jerry == 3:
#             skip_jerry = 0
#             jerry_rest = False
#             tj.append("Jerry")
#             if len(tj) == 2 and tj != tj_copy:
#                 tj = tj_copy.copy()
        
    
#     if tom_rest and jerry_rest:
#         continue
    
#     if area_map[coordinates[0]][coordinates[1]] == "W":
#         print(f"{tj[turn]} hits a wall and needs to rest.")
#         if tj[turn] == "Tom":
#             tom_rest = True
#             tj.remove("Tom")
#         elif tj[turn] == "Jerry":
#             jerry_rest = True
#             tj.remove("Jerry")
#         if len(tj) == 1:
#             turn = 0
#         if len(tj) == 0:
#             continue
        
#     elif area_map[coordinates[0]][coordinates[1]] == "T":
#         loser = tj[turn]
#         if loser == "Jerry":
#             winner = "Tom"
#         else:
#             winner = "Jerry"
#         print(f"{loser} is out of the game! The winner is {winner}." )
#         break
#     elif area_map[coordinates[0]][coordinates[1]] == "E":
#         print(f"{tj[turn]} found the Exit and wins the game!")
#         break
    
#     if not tom_rest and not jerry_rest:
#         turn += 1
#         if turn == 2:
#             turn = 0
