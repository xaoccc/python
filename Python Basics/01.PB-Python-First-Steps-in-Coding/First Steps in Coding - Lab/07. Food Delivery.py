pile = 10.35
riba = 12.40
zelen = 8.15
dostavka = 2.5

pile_q = int(input())
riba_q = int(input())
zelen_q = int(input())

osnovno = (pile * pile_q) + (riba * riba_q) + (zelen * zelen_q)
desert = osnovno*0.2

total = osnovno + desert + dostavka
print(total)
