num = int(input())
sum_num = 0

for i in range(num):
    num_input = float(input())
    sum_num += num_input
print(f"{(sum_num / num):.2f}")