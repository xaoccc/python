arr = []
operations = 0

for i in range(n):
    arr.append((2 * i) + 1)
            
while min(arr) != max(arr):
    arr[arr.index(max(arr))] -= 1
    arr[arr.index(min(arr))] += 1
    operations += 1

return operations


# return ( n * n ) // 4
