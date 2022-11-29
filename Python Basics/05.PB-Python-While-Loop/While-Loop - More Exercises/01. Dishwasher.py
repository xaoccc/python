wash_bottles = int(input())
wash_q = wash_bottles * 750
loading = 0
wash_used = 0
plates_washed = 0
pots_washed = 0

while wash_q >= wash_used:
    kitchenware = input()
    if kitchenware == "End":
        print("Detergent was enough!")
        print(f"{plates_washed} dishes and {pots_washed} pots were washed.")
        print(f"Leftover detergent {wash_q - wash_used} ml.")
        break
    kitchenware = int(kitchenware)
    loading += 1

    if loading % 3 == 0:
        wash_used += kitchenware * 15
        pots_washed += kitchenware
    else:
        wash_used += kitchenware * 5
        plates_washed += kitchenware

else:
    print(f"Not enough detergent, {wash_used - wash_q} ml. more necessary!")
