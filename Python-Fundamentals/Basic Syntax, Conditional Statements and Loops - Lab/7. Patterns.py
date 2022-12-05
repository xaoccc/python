#We use normal loops instead of nested loops, because hre we have 2 x Linear Time — O(2*n), in nested loops we have 2 x Quadratic Time — O(2*n²) , 
#because in furst case we have 2 loops, in second one we have 2 nested loops, so time complexity = O(2*n)
#Thus we optimize time complexity, also we use 5 lines instead of 9 lines -> space complexity = O(2*n) as well
num = int(input())
for i in range(num+1):
  print("*" * i)
for i in range(num-1, 0, -1):
  print("*" * i)
