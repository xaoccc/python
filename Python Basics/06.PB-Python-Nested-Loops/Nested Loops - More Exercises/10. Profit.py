one = int(input())   
two = int(input())
five = int(input())
sum = int(input())

for i in range(0, one + 1):
  one_sum = 1 * i
  for j in range(0, two + 1):
    two_sum = 2 * j
    for k in range(0, five + 1):
      five_sum = 5 * k
      current_sum = one_sum + two_sum + five_sum
      if sum == current_sum:
        print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sum} lv.")