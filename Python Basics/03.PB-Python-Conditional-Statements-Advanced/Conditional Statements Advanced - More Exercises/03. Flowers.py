#user input
hrizant = int(input())
roza = int(input())
lale = int(input())
season = input().lower()
hol = input().lower()
total_sum = 0

#logic
flowers = hrizant + roza + lale
if season == "spring" or season == "summer" :
    total_sum = (hrizant * 2) + (roza * 4.10) + (lale * 2.5)
    if season == "spring" and lale > 7:
        total_sum -= total_sum * 0.05
elif season == "autumn" or season == "winter" :
    total_sum = (hrizant * 3.75) + (roza * 4.50) + (lale * 4.15)
    if season == "winter" and roza >= 10:
        total_sum -= total_sum * 0.1
if hol == "y" :
        total_sum *= 1.15
if flowers > 20 :
    total_sum -= total_sum * 0.2
    
#output
print(f"{(total_sum + 2):.2f}")
    

