guests_num = int(input())
guests_list = []
guests_arrived = []

while len(set(guests_list)) < guests_num:
    code = input()
    if len(code) == 8:
        guests_list.append(code)
    
code = input()
while code != "END":
    if len(code) == 8:
        guests_arrived.append(code)
    code = input()
result = sorted(set(guests_list) - set(guests_arrived))    
print(len(result))
print(*result, sep="\n")
