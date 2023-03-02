command = input()
dwarfery, dwarves_total, hat_color_num = {}, [], []

def dwarfery_entry(dwarf_name, dwarf_hat_color, dwarf_physics):
    if dwarf_name not in dwarfery:
        dwarfery[dwarf_name] = {dwarf_hat_color: dwarf_physics}
    else:
        if dwarf_hat_color not in dwarfery[dwarf_name] or dwarfery[dwarf_name][dwarf_hat_color] < dwarf_physics:
            dwarfery[dwarf_name][dwarf_hat_color] = dwarf_physics

while command != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = [int(el) if el.isdigit() else el for el in command.split(" <:> ")]
    dwarfery_entry(dwarf_name, dwarf_hat_color, dwarf_physics)
    command = input()

for dwarf in dwarfery:
    for dwarf_hat, dwarf_power in dwarfery[dwarf].items():
        dwarves_total.append([dwarf, dwarf_hat, dwarf_power])
for i in dwarves_total:
    hat_color_num.append(i[1])
for i in range(len(hat_color_num)):
    dwarves_total[i].append(hat_color_num.count(hat_color_num[i]))

dwarves_sorted = sorted(dwarves_total, key=lambda x: (-x[2], -x[3]))        

for i in dwarves_sorted:
    print(f"({i[1]}) {i[0]} <-> {i[2]}")
