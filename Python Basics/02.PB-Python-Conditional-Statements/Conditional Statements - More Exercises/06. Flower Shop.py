#user input
magnol = int(input())
zumbul = int(input())
rose = int(input())
cactus = int(input())
gift_price = float(input())
magnol_price = 3.25
zumbul_price = 4
rose_price = 3.5
cactus_price = 8
import math

#logic and output
budget = (magnol * magnol_price) + (zumbul * zumbul_price) + (rose * rose_price) + (cactus * cactus_price)
budget = budget * 0.95
if budget >= gift_price :
    print(f"She is left with {math.floor(budget - gift_price)} leva.")
else :
    print(f"She will have to borrow {math.ceil(gift_price - budget)} leva." )