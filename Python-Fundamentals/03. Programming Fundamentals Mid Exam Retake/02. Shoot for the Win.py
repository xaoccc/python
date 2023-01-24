targets  = input().split()
targets = [int(i) for i in targets]
shots_index_list = []
shot_targets_list = []
command = input()
while command != "End":
    shot_index = int(command)
    if shot_index >= len(targets):
        continue
    else:
        if shot_index not in shots_index_list:
            
            for i in range(len(targets)):
                if i == shot_index:
                    continue
                if i not in shots_index_list:
                    if targets[i] > targets[shot_index]:
                        targets[i] -= targets[shot_index]
                    elif targets[i] <= targets[shot_index]:
                        targets[i] += targets[shot_index]
            
            targets[shot_index] = -1
            
            shots_index_list.append(shot_index)
    command = input()
    
for i in range(len(shots_index_list)):    
    shot_targets_list.append(targets[shots_index_list[i]])
    
shot_targets_num = len(shots_index_list)
targets = [str(i) for i in targets]
targets = " ".join(targets)
    
print(f"Shot targets: {shot_targets_num} -> {targets}")
