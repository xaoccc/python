numbers = [float(i) for i in input().split()]

result = []
i = 0
while i < len(numbers):
    j = i + 1
    # check if there are adjacent equal numbers
    while j < len(numbers) and numbers[j] == numbers[i]:
        j += 1
    # sum the adjacent equal numbers and add to the result
    sum_adj = sum(numbers[i:j])
    result.append(sum_adj)
    # check if the obtained sum is equal to its neighbors and sum them
    while len(result) > 1 and result[-1] == result[-2]:
        sum_adj = result.pop() + result.pop()
        result.append(sum_adj)
    i = j
print(*result)
