targets = [int(i) for i in input().split()]
action = input()

while action != "End":
    action = action.split()
    target = int(action[1])
    action_data = int(action[2])
    
    if action[0] == "Shoot":
        if target > -1 and target < len(targets):
            if action_data < targets[target]:
                targets[target] -= action_data
            elif action_data >= targets[target]:
                del targets[target]
        else:
            pass
        
    elif action[0] == "Strike":
        if (target - action_data) > -1 and (target + action_data) < len(targets):
            del targets[target - action_data : target + action_data + 1]
        else:
            print("Strike missed!")
        
    elif action[0] == "Add":
        if target > -1 and target < len(targets):
            targets.insert(target, action_data)
        else:
            print("Invalid placement!")
    action = input()
    
targets = [str(i) for i in targets]    
print("|".join(targets))
