size = int(input())
ships_list = []
hits = 0

for i in range(size):
    ships = [int(i) for i in input().split()]
    ships_list.append(ships)
attacks = input().split()
for i in range(len(attacks)):
    current_attack = attacks[i].split("-")
    if ships_list[int(current_attack[0])][int(current_attack[1])] > 0:
        ships_list[int(current_attack[0])][int(current_attack[1])] -= 1
        if ships_list[int(current_attack[0])][int(current_attack[1])] == 0:
            hits += 1
print(hits)
