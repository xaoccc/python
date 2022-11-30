clients_num = int(input())
all_clients_amount = 0
 
for i in range(clients_num):
    products_num = 0
    total_amount = 0
 
    while True:
        purchase = input()
        if purchase == "Finish":
            if products_num % 2 == 0:
                total_amount *= 0.8
            all_clients_amount += total_amount
            print(f"You purchased {products_num} items for {total_amount:.2f} leva.")
            break
        if purchase == "basket":
            total_amount += 1.5
        if purchase == "wreath":
            total_amount += 3.8
        if purchase == "chocolate bunny":
            total_amount += 7
        products_num += 1
 
average_amount = all_clients_amount / clients_num
print(f"Average bill per client is: {average_amount:.2f} leva.")
