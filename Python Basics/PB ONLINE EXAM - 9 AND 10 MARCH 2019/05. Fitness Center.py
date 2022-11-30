visitors_num = int(input())
training_back = 0
training_chest = 0
training_legs = 0
training_abs = 0
buyed_protein_shake = 0
buyed_protein_bar = 0
visitors_num_total = 0
for i in range(visitors_num):
    visitor_activity = input()
    visitors_num_total += 1
    if visitor_activity == "Back":
        training_back += 1
    if visitor_activity == "Chest":
        training_chest += 1
    if visitor_activity == "Legs":
        training_legs += 1
    if visitor_activity == "Abs":
        training_abs += 1
    if visitor_activity == "Protein shake":
        buyed_protein_shake += 1
    if visitor_activity == "Protein bar":
        buyed_protein_bar += 1
visitors_training = training_back + training_chest + training_legs + training_abs
visitors_proteining = buyed_protein_shake + buyed_protein_bar
print(f"{training_back} - back")
print(f"{training_chest} - chest")
print(f"{training_legs} - legs")
print(f"{training_abs} - abs")
print(f"{buyed_protein_shake} - protein shake")
print(f"{buyed_protein_bar} - protein bar")
print(f"{visitors_training * 100 / visitors_num_total}% - work out")
print(f"{visitors_proteining * 100 / visitors_num_total}% - protein")
