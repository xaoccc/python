while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    money_saved = 0
    while money_saved < budget:
        money_saved += float(input())
    else:
        print(f"Going to {destination}!")