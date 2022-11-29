cake_width = int(input())
cake_lenght = int(input())
pieces = cake_width * cake_lenght
total_pieces_eaten = 0

while pieces > 0:
    pieces_eaten = input()
    if pieces_eaten == "STOP":
        print(f"{pieces} pieces are left.")
        break
    pieces -= int(pieces_eaten)

else:    
    print(f"No more cake left! You need {abs(pieces)} pieces more.")