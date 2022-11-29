#user input
capacity = int(input())
fans_total = int(input())
fan_a = 0
fan_b = 0
fan_v = 0
fan_g = 0


#logic
for i in range (1, fans_total + 1) :
    sector = input()
    if sector == "A" :
        fan_a += 1
    elif sector == "B" :
        fan_b += 1
    elif sector == "V" :
        fan_v += 1
    elif sector == "G" :
        fan_g += 1

#print output
print(f"{(fan_a * 100/ fans_total):.2f}%")
print(f"{(fan_b * 100/ fans_total):.2f}%")
print(f"{(fan_v * 100/ fans_total):.2f}%")
print(f"{(fan_g * 100/ fans_total):.2f}%")
print(f"{(fans_total * 100/ capacity):.2f}%")