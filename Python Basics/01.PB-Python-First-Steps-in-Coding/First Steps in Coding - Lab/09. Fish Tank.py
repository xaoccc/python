l = int(input())
w = int(input())
h = int(input())
perc = float(input())
v = l * w * h
vlit = v / 1000
liters = vlit * (1 - (perc/100))
print(liters)
