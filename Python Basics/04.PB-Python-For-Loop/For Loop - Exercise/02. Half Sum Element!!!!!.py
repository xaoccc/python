n = int(input())
import sys
# 1.Create two variables:"max_num" with very low value, in which we keep the biggest number and "sum_numbers"=0, in which we keep the sum of inputs:
sum_numbers = 0
max_num = -sys.maxsize
# 2.After we get the number of inputs – n, we loop from 0 to n, as we input "num" on each iteration:
for i in range (n) :
    num = int(input())
#3.Inside the loop we are checking if "num" is greater than "max_num". If greater, then "max_num" ill be equal to "num". 
    if num > max_num :
        max_num = num
    #After this we add each "num" into "sum_numbers" (out of if, because we do this unconditionally for all "num"):
    sum_numbers += num
#4.After the loop we finally have the final "sum_numbers" and the final "max_num" and we can finally check if... :
if max_num == sum_numbers - max_num :
    print ("Yes")
    print (f"Sum = {max_num}")
# 5.If they are not equal, we print the difference (positive number, using abs() function):
else :
    print ("No")
    sum_others = sum_numbers - max_num
    print (f"Diff = {abs(sum_others - max_num)}")
