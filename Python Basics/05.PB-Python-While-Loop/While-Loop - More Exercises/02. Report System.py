sum_needed = int(input())
total_sum_CS = 0
total_sum_CC = 0
average_CS = 0
average_CC = 0
transaction_num_CC = 0
transaction_num_CS = 0
transaction_num = 0

while (total_sum_CS + total_sum_CC) < sum_needed:
    product_price = input()
    if product_price == "End":
        print("Failed to collect required money for charity.")
        break
    transaction_num += 1
    product_price = int(product_price)
    if transaction_num % 2 == 0:
        if product_price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_sum_CC += product_price
            transaction_num_CC += 1
    else:
        if product_price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total_sum_CS += product_price
            transaction_num_CS += 1
else:
    average_CS = total_sum_CS / transaction_num_CS
    average_CC = total_sum_CC / transaction_num_CC
    print(f"Average CS: {average_CS:.2f}")
    print(f"Average CC: {average_CC:.2f}")
