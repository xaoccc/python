n = int(input())
result = [0, 1, 1]

def fib(i):
    global result
    if i < 1:
        return 1
    result.append(fib(i - 2) + fib(i - 1))
    current_num = result[-1]
    return current_num

fib(n)
print(result[:3] + result[-n:])
