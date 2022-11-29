#input
n = int(input())
sum1 = 0
sum2 = 0
is_equal = ""

#logic
for i in range (0, n):
    n1 = int(input())
    sum1 += n1
for i in range (0, n):
    n2 = int(input())
    sum2 += n2
if sum1 == sum2 :
    is_equal = f"Yes, sum = {sum1}"
else :
    is_equal = f"No, diff = {abs(sum1-sum2)}"
#output
print(is_equal)
