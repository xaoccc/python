flour_price = float(input())
flour_q = float(input())
sugar_q = float(input())
eggs_pack = int(input())
yeast = int(input())
sugar_price = flour_price * 0.75
eggs_pack_price = flour_price * 1.1
yeast_price = sugar_price * 0.2
total_price = (flour_price * flour_q) +\
    (sugar_price * sugar_q) +\
    (eggs_pack_price * eggs_pack) +\
    (yeast_price * yeast)
print(f"{total_price:.2f}")
