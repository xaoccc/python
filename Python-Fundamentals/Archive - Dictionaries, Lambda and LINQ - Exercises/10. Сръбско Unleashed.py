payneer = {}
command = input()
while command != "End":
    command = command.split("@")
    singer = command[0].strip(" ")
    command[1] = command[1].split()
    if len(command[1]) >= 3 and command[1][-2].isdigit():
        place = " ".join(command[1][ :len(command[1])-2])
        ticket_price = int(command[1][-2])
        ticket_count = int(command[1][-1])
        if place not in payneer:
            payneer[place] = {singer: ticket_price * ticket_count}
        else:
            if singer not in payneer[place]:
                payneer[place][singer] = ticket_price * ticket_count
            else:
                payneer[place][singer] += ticket_price * ticket_count
    
    command = input()
for chalga in payneer:
    payneer[chalga] = dict(sorted(payneer[chalga].items(), key=lambda x: -x[1]))
    
for chalga in payneer:
    print(chalga)
    for key, value in payneer[chalga].items():
        print(f"#  {key} -> {value}")
