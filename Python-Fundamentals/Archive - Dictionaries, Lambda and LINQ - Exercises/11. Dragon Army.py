dragons_num = int(input())
dragons_data, sorted_data = {}, {}

for i in range(dragons_num):
    type, name, damage, health, armor = [int(dragon) if dragon.isdigit() else dragon for dragon in input().split()]
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    dragons_current_data = [damage, health, armor]
    if type not in dragons_data:
        dragons_data[type] = {name: dragons_current_data}
    else:
        dragons_data[type][name] = dragons_current_data

for i in dragons_data:
    sorted_data[i] = dict(sorted(dragons_data[i].items(), key=lambda x: x[0]))
for i in sorted_data:
    total_damage, total_health, total_armor = 0, 0, 0

    for j in sorted_data[i]:
        total_damage += sorted_data[i][j][0]
        total_health += sorted_data[i][j][1]
        total_armor += sorted_data[i][j][2]

    print(f"{i}::({total_damage / len(sorted_data[i]):.2f}/{total_health / len(sorted_data[i]):.2f}/{total_armor / len(sorted_data[i]):.2f})")
    for j in sorted_data[i]:
        print(f"-{j} -> damage: {sorted_data[i][j][0]}, health: {sorted_data[i][j][1]}, armor: {sorted_data[i][j][2]}")
