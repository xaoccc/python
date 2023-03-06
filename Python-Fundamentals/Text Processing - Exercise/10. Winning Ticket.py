tickets = ' '.join(input().split()).split(", ")

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if ticket == '@' * 20 or ticket == '#' * 20 or ticket == '$' * 20 or ticket == '^' * 20:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        
        elif ticket.count("@") >= 12:
            if "@" * 6 in ticket[ :11] and "@" * 6 in ticket[10: ]:
                print(f'ticket "{ticket}" - {ticket[10: ].count("@")}{"@"}')
        elif ticket.count("$") >= 12:
            for i in range(5, 10, -1):
                if "$" * i in ticket[ :11] and "$" * i in ticket[10: ]:
                    print(f'ticket "{ticket}" - {i}{"$"}')
                    break
        else:
            print(f'ticket "{ticket}" - no match')
