guests = int(input())
price = float(input())
budget = float(input())
if 10 <= guests <= 15:
    price *= 0.85
elif 15 < guests <= 20:
    price *= 0.80
elif guests > 20:
    price *= 0.75
cake = budget * 0.1
total = (guests * price) + cake
if total <= budget:
    print(f"It is party time! {budget-total:.2f} leva left.")
else:
    print(f"No party! {total-budget:.2f} leva needed.")
