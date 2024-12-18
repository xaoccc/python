def fib(num):
    if num == 1 or num == 0:
        return num
    return fib(num-1) + fib(num-2)

print(fib(7))