#user input
juniors = int(input())
seniors = int(input())
trace = input()

#logic
if trace == "trail" :
    total_sum = (juniors * 5.50) + (seniors * 7)
elif trace == "cross-country" :
    total_sum = (juniors * 8) + (seniors * 9.50)
elif trace == "downhill" :
    total_sum = (juniors * 12.25) + (seniors * 13.75)
elif trace == "road" :
    total_sum = (juniors * 20) + (seniors * 21.50)
    
if trace == "cross-country" and (juniors + seniors) >= 50 :
    total_sum -= total_sum * 0.25
total_sum -= total_sum * 0.05

#output
print(f"{total_sum:.2f}")