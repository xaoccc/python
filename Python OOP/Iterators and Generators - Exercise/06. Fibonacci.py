def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        result = num1 + num2
        yield num1
        num1, num2 = num2, result


