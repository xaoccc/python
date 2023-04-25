inputs = [int(i) for i in input().split(", ")]
matrix = []
for i in range(inputs[0]):
    matrix.append([int(j) for j in input().split()])
for i in range(inputs[1]):
    sum = 0
    for j in range(inputs[0]):
        sum += matrix[j][i]
    print(sum)
