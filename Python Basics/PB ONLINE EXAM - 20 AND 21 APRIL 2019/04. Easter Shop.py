eggs_avail = int(input())
sold_eggs_total = 0
purch_eggs_total = 0
while True:
    action = input()
    if action == "Close":
        print("Store is closed!")
        print(f"{sold_eggs_total} eggs sold.")
        break
    if action == "Buy":
        sold_eggs = int(input())
        sold_eggs_total += sold_eggs
        if eggs_avail >= sold_eggs:
            eggs_avail -= sold_eggs
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_avail}.")
            break
    elif action == "Fill":
        purch_eggs = int(input())
        eggs_avail += purch_eggs
