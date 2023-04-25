def find_symbol(rows, matrix):
    for i in range(rows):
        matrix.append(list(input()))
    symbol = input()
    for i in range(rows):
        if symbol in matrix[i]:
            return (i, matrix[i].index(symbol))
    return f"{symbol} does not occur in the matrix"
print(find_symbol(int(input()), []))
