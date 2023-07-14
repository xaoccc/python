def fibonacci():
    num1 = 0
    num2 = 1
    for i in range(5):
        result = num1 + num2
        num1, num2 = num2, result
        yield num1, num2


generator = fibonacci()
for i in range(1):
    print(next(generator))
