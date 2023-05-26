def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    result, items = "", 0
    for item, (price, quantity) in kwargs.items():
        if price * quantity <= budget:
            result += f"You bought {item} for {price * quantity:.2f} leva.\n"
            budget -= price * quantity
            items += 1
            if items == 5:
                return result
    return result
