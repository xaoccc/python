#user input
loads_num = int(input())
freight_rate = 0
tons_van = 0
tons_truck = 0
tons_train = 0
total_weight = 0

#logic
for load in range (1, loads_num + 1) :
    current_load_weight = int(input())
    if current_load_weight < 4 :
        tons_van += current_load_weight
        freight_rate += 200 * current_load_weight
    elif 4 <= current_load_weight <= 11 :
        tons_truck += current_load_weight
        freight_rate += 175 * current_load_weight
    else :
        tons_train += current_load_weight
        freight_rate += 120 * current_load_weight
    total_weight += current_load_weight
avg_freigt_rate = freight_rate / total_weight

#print output
print(f"{avg_freigt_rate:.2f}")
print(f"{(tons_van * 100/ total_weight):.2f}%")
print(f"{(tons_truck * 100/ total_weight):.2f}%")
print(f"{(tons_train * 100/ total_weight):.2f}%")