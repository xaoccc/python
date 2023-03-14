import re
demons = [x.strip() for x in input().split(",")]
pattern_sum = r'([0-9]+\.[0-9]+)|([1-9][0-9]*)|(-[0-9]+\.[0-9]+)|(-[1-9][0-9]*)'
pattern_other = r'[\*\/]'
not_in_name = ["-", "+", "*", "/", "."]
demons_data = {}

for demon in demons:
    demon_health, demon_damage, damage_decode = 0, 0, ""
    decode_sum = re.finditer(pattern_sum, demon)
    decode_other = re.finditer(pattern_other, demon)

    for i in decode_sum:
        if i[0] != "-":
            demon_damage += float(i.group())
        else:
            demon_damage -= float(i.group()[1: ])
    for i in decode_other:
        if i.group() == "*":
            demon_damage *= 2
        elif i.group() == "/":
            demon_damage /= 2
    for j in demon:
        if not j.isdigit() and j not in not_in_name:
            demon_health += ord(j)
    demons_data[demon] = [demon_health, demon_damage]
   
sorted_demons_data = dict(sorted(demons_data.items(), key=lambda x: x[0]))

for demon_name, demon_stats in sorted_demons_data.items():
    print(f"{demon_name} - {demon_stats[0]} health, {demon_stats[1]:.2f} damage")




# import re
# demons = [x.strip() for x in input().split(",")]
# pattern = r'([\-\+\*\/])|([0-9]+\.[0-9]+)|([1-9][0-9]*)'
# not_in_name = ["-", "+", "*", "/", "."]
# demons_data = {}

# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False


# for demon in demons:
#     demon_health, demon_damage, decode_list, damage_decode = 0, 0, [], ""
#     decode = re.finditer(pattern, demon)

#     for i in decode:
#         decode_list.append(i.group())
#     for i in range(len(decode_list)):
#         if isfloat(decode_list[i]) and i == 0:
#             demon_damage = float(decode_list[i])
#         elif isfloat(decode_list[i]) and decode_list[i - 1] == "-":
#             demon_damage -= float(decode_list[i])
#         elif isfloat(decode_list[i]) and decode_list[i - 1] != "-":
#             demon_damage += float(decode_list[i])
            
#     for i in range(len(decode_list)):    
#         if decode_list[i] == "*":
#             demon_damage *= 2
#         elif decode_list[i] == "/":
#             demon_damage /= 2

#     for j in demon:
#         if not j.isdigit() and j not in not_in_name:
#             demon_health += ord(j)
#     demons_data[demon] = [demon_health, demon_damage]
   
# sorted_demons_data = dict(sorted(demons_data.items(), key=lambda x: x[0]))

# for demon_name, demon_stats in sorted_demons_data.items():
#     print(f"{demon_name} - {demon_stats[0]} health, {demon_stats[1]:.2f} damage")

