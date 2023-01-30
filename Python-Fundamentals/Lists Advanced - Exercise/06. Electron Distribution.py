electrons_num = int(input())
shells = []
i = 0

while electrons_num > 0:
    i += 1
    shell_value = 2 * i ** 2

    if electrons_num >= shell_value:
        shells.append(shell_value)
        electrons_num -= shell_value
    else:
        shells.append(electrons_num)
        electrons_num = 0
        
print(shells)
