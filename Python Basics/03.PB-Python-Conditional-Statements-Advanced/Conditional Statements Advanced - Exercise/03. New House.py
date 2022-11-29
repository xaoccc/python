flower_type = input()
flowers_number = int(input())
budget = int(input())
flowers_cost = 1

roses_price = 5
dahlias_price = 3.8
tulips_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

if flower_type == "Roses" :
    flowers_cost = flowers_number * roses_price
    if flowers_number > 80 :
        flowers_cost *=  0.9
if flower_type == "Dahlias" :
    flowers_cost = flowers_number * dahlias_price
    if flowers_number > 90 :
        flowers_cost *=  0.85
if flower_type == "Tulips" :
    flowers_cost = flowers_number * tulips_price
    if flowers_number > 80 :
        flowers_cost *= 0.85
if flower_type == "Narcissus" :
    flowers_cost = flowers_number * narcissus_price
    if flowers_number < 120 :
        flowers_cost *= 1.15
if flower_type == "Gladiolus" :
    flowers_cost = flowers_number * gladiolus_price
    if flowers_number < 80 :
        flowers_cost *= 1.2
#output
if flowers_cost <= budget :
    print (f"Hey, you have a great garden with {flowers_number} {flower_type} and {budget-flowers_cost:.2f} leva left.")
elif flowers_cost > budget :
    print (f"Not enough money, you need {flowers_cost-budget:.2f} leva more.")