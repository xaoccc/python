#user input
budget = float(input())
stat = int(input())
obleklo_cena = float(input())

#logic and output
if stat <= 150 :
    stat_obleklo_cena = stat * obleklo_cena
    if budget < stat_obleklo_cena + (budget * 0.1) :
        mneed = (stat_obleklo_cena + (budget * 0.1) - budget)
        print ("Not enough money!")
        print (f"Wingard needs {mneed:.2f} leva more.")
    else :
        mleft = budget - (stat_obleklo_cena + (budget * 0.1))
        print ("Action!")
        print (f"Wingard starts filming with {mleft:.2f} leva left.")
else :
    obleklo_cena = obleklo_cena - (obleklo_cena*0.1)
    stat_obleklo_cena = stat * obleklo_cena
    if budget < stat_obleklo_cena + (budget * 0.1) :
        mneed = stat_obleklo_cena + ((budget * 0.1) - budget)
        print ("Not enough money!")
        print (f"Wingard needs {mneed:.2f} leva more.")
    else :
        mleft = budget - (stat_obleklo_cena + (budget * 0.1))
        print ("Action!")
        print (f"Wingard starts filming with {mleft:.2f} leva left.")
