lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
for loss_num in range(1, lost_fights_count + 1):
  if loss_num % 2 == 0:
    total_price += helmet_price
  if loss_num % 3 == 0:
    total_price += sword_price
  if loss_num % 6 == 0:
    total_price += shield_price
  if loss_num % 12 == 0:
    total_price += armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
