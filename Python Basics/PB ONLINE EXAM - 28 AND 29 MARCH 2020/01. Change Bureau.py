bitcoins = int(input())
yuans = float(input())
comiss = float(input())
 
levs_b = bitcoins * 1168
dollars = yuans * 0.15
levs_y = dollars * 1.76
euro = (levs_b + levs_y) / 1.95
euro -= (euro * comiss / 100)
print(f"{euro:.2f}")
