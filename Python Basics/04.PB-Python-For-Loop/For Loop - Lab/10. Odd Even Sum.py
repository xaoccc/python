#input
n = int(input())
sum_even = 0
sum_odd = 0

#logic
for i in range (0, n):
    current_number = int(input())
    if i % 2 == 0 :
        sum_even = current_number + sum_even
    else :
        sum_odd = current_number + sum_odd
#comparing both sums and output
if sum_even == sum_odd :
    print("Yes")
    print(f"Sum = {sum_even}")
else :
    print("No")
    print(f"Diff = {abs(sum_even - sum_odd)}")
