#input
n = int(input())
sum1 = 0
sum2 = 0

#logic
for i in range (0, n):
    current_number = int(input())
#sum of the even numbers
    if i % 2 == 0 :
        sum1 = current_number + sum1
#sum of the odd numbers
    else :
        sum2 = current_number + sum2
#comparing both sums and output
if sum1 == sum2 :
    print("Yes")
    print(f"Sum = {sum1}")
else :
    print("No")
    if sum1 > sum2 :
        print(f"Diff = {sum1-sum2}")
    elif  sum1 < sum2 :
        print(f"Diff = {sum2-sum1}")




