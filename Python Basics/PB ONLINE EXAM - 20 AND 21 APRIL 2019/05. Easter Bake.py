from math import ceil
easter_bread_num = int(input())
total_sugar = 0
total_flour = 0
max_flour = -10000000
max_sugar = -10000000
 
for i in range(easter_bread_num):
    sugar = int(input())
    flour = int(input())
    total_sugar += sugar
    total_flour += flour
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
needed_sugar_packs = ceil(total_sugar / 950)
needed_flour_packs = ceil(total_flour / 750)
print(f"Sugar: {needed_sugar_packs}")
print(f"Flour: {needed_flour_packs}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
