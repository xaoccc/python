people_waiting = int(input())
lift_state = input().split()
lift_state = [int(i) for i in lift_state]
lift_taken_places = 0
lift_full = False
    
for i in range(len(lift_state)):
    if lift_state[i] == 4:
        lift_taken_places += 4
        continue
    else:
        if people_waiting >= 4:
            people_waiting -= (4 - lift_state[i])
            lift_state[i] += 4 - lift_state[i]
            lift_taken_places += 4
        elif people_waiting == 0:
            break
        elif 0 < people_waiting < 4:
            if people_waiting > 4 - lift_state[i]:
                people_waiting -= (4 - lift_state[i])
                lift_taken_places += 4
            else:
                lift_state[i] += people_waiting
                people_waiting -= people_waiting
                lift_taken_places += lift_state[i]
                break

if lift_taken_places == 4 * len(lift_state):
    lift_full = True
            
lift_state = " ".join([str(i) for i in lift_state])
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{lift_state}")
elif people_waiting == 0 and lift_full == True:
    print(lift_state)
else:
    print(f"The lift has empty spots!\n{lift_state}")
