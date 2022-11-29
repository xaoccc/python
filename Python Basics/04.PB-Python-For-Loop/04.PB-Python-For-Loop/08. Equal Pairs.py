#user input
n = int(input())
#The first pair should be outside the loop, so we can store its value and compare it with the second one
num1 = int(input())
num2 = int(input())
#Here is the first sum value
sum_num = num1 + num2
#We are defining each difference between sums and the greatest of these differences
diff = 0
max_diff = 0

#logic
for pair in range (n-1) :
    num1 = int(input())
    num2 = int(input())
    current_sum = num1 + num2
#After we created a second sum variable - current_sum - this time we are in the loop and we start comparing each pair sum with the previous one 
    if current_sum != sum_num :
        diff = abs(sum_num - current_sum) 
        sum_num = current_sum
    if diff > max_diff :
        max_diff = diff
if diff == 0:
    print(f"Yes, value={sum_num}")
else :
    print(f"No, maxdiff={max_diff}")