import re
demons = [x.strip() for x in input().split(",")]
pattern = r'([\-\+\*\/])|([0-9]+\.[0-9]+)|([1-9][0-9]*)'
demons_data = {}

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


for demon in demons:
    demon_health = 0
    demon_damage = 0
    decode_list = []
    damage_decode = ""
    decode = re.finditer(pattern, demon)

    for i in decode:
        decode_list.append(i.group())
    for i in range(len(decode_list)):
        if isfloat(decode_list[i]) and i == 0:
            demon_damage = float(decode_list[i])
        elif decode_list[i] == "-":
            demon_damage -= float(decode_list[i + 1])
        elif decode_list[i] == "+":
            demon_damage += float(decode_list[i + 1])
        elif decode_list[i] == "*":
            demon_damage *= 2
        elif decode_list[i] == "/":
            demon_damage /= 2
        else:
            demon_damage += float(decode_list[i])

    for j in demon:
        if j.isalpha():
            demon_health += ord(j)
    demons_data[demon] = [demon_health, demon_damage]

print(demons_data)

