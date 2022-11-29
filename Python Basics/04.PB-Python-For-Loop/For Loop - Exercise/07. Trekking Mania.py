#user input

n = int(input())
climber_groups_num = n
musala = 0
monbl = 0
kilim = 0
k_two = 0
everest = 0
group_total = 0


#logic
for i in range (0, n) :
    group_num = int(input())
    if group_num <= 5 :
        musala += group_num
    elif 5 < group_num <= 12 :
        monbl += group_num
    elif 12 < group_num <= 25 :
        kilim += group_num
    elif 25 < group_num <= 40 :
        k_two += group_num
    elif group_num > 40 :
        everest += group_num
    group_total += group_num

#print output
print(f"{(musala*100/group_total):.2f}%")
print(f"{(monbl*100/group_total):.2f}%")
print(f"{(kilim*100/group_total):.2f}%")
print(f"{(k_two*100/group_total):.2f}%")
print(f"{(everest*100/group_total):.2f}%")