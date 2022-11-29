#input
n = int(input())
sum = 0

#logic
for i in range (0, n):
    current_num = int(input())
    sum = current_num + sum

#output
print(sum)