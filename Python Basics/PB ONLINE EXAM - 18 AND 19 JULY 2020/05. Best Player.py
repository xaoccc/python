max_goals = -1
best_player = ""
 
while max_goals < 10:
    player = input()
    if player == "END":
        break
    goals = int(input())
    if max_goals < goals:
        best_player = player
        max_goals = goals
 
 
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
