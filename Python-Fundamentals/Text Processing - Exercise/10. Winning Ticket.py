tickets = ' '.join(input().split()).split(", ")

def winner(symbol):
    for i in range(11, 5, -1):
        if symbol * i in ticket[ :10] and symbol * i in ticket[10: ]:
            print(f'ticket "{ticket}" - {i}{symbol}')
            break
    else:
        print(f'ticket "{ticket}" - no match')

for ticket in tickets:
    ticket = ticket.replace(" ", "")
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if ticket == '@' * 20 or ticket == '#' * 20 or ticket == '$' * 20 or ticket == '^' * 20:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        
        elif ticket.count("@") >= 12:
            winner("@")
            
        elif ticket.count("$") >= 12:
            winner("$")
            
        elif ticket.count("#") >= 12:
            winner("#")
            
        elif ticket.count("^") >= 12:
            winner("^")
            
        else:
            print(f'ticket "{ticket}" - no match')
