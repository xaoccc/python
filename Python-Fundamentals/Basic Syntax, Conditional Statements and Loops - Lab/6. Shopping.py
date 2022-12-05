budget = int(input())
while True:
  product_price = input()
  if product_price == "End":
    print("You bought everything needed.")
    break
  budget -= int(product_price)
  if budget < 0:
    print("You went in overdraft!")
    break
