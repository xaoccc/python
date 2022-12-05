#We use two loops instead of one nestd loop, because hre we have Linear Time — O(n), in nested loops we have Quadratic Time — O(n²)
#Thus we optimize time complexity
num = int(input())
for i in range(num+1):
  print("*" * i)
for i in range(num-1, 0, -1):
  print("*" * i)
