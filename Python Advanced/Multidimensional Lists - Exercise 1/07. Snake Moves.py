rows, cols = [int(i) for i in input().split()]
snake = input()

total_digits = rows * cols
snake_total = snake * (total_digits // len(snake)) + snake[ : total_digits % len(snake)]

for row in range(0, total_digits, cols):
    if (row // cols) % 2 == 0:
        print(snake_total[row : row + cols])
    else:
        print(snake_total[row : row + cols][::-1])
