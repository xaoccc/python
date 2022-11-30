games_num = int(input())
hearthstone_sales = 0
fornite_sales = 0
overwatch_sales = 0
others_sales = 0
total_sales = 0
for i in range(games_num):
    game = input()
    total_sales += 1
    if game == "Hearthstone":
        hearthstone_sales += 1
    elif game == "Fornite":
        fornite_sales += 1
    elif game == "Overwatch":
        overwatch_sales += 1
    else:
        others_sales += 1
#output
print(f"Hearthstone - {hearthstone_sales * 100 / total_sales:.2f}%")
print(f"Fornite - {fornite_sales * 100 / total_sales:.2f}%")
print(f"Overwatch - {overwatch_sales * 100 / total_sales:.2f}%")
print(f"Others - {others_sales * 100 / total_sales:.2f}%")
