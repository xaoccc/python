from collections import deque
elf_energy, materials = deque([int(i) for i in input().split()]), deque([int(i) for i in input().split()])
total_energy_used, toys, try_num = 0, 0, 0

while elf_energy and materials:
    current_elf_energy, current_material = elf_energy.popleft(), materials.pop()
    try_num += 1
    
    if current_elf_energy < 5:
        materials.append(current_material)
        try_num -= 1
    
    elif current_elf_energy < current_material and try_num % 3 != 0:
        materials.append(current_material)
        elf_energy.append(2 * current_elf_energy)
        
    elif try_num % 3 == 0 and current_elf_energy < (2 * current_material):
        materials.append(current_material)
        elf_energy.append(2 * current_elf_energy)
        
    else:
        if current_elf_energy >= current_material and try_num % 3 != 0:
            if try_num % 5 != 0:
                toys += 1
                elf_energy.append(current_elf_energy - current_material + 1)
            else:
                elf_energy.append(current_elf_energy - current_material)
            total_energy_used += current_material

        elif try_num % 3 == 0 and current_elf_energy >= (2 * current_material):
            if try_num % 5 != 0:
                toys += 2
                elf_energy.append(current_elf_energy - (2 * current_material) + 1)
            else:
                elf_energy.append(current_elf_energy - (2 * current_material))
            total_energy_used += (2 * current_material)

print(f"Toys: {toys}")
print(f"Energy: {total_energy_used}")
if elf_energy:
    print(f"Elves left: {', '.join([str(i) for i in elf_energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(i) for i in materials])}") 
