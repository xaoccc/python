def fibonacci(num = int(input())):
    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    else:
        fib_seq = [1, 1]
        for i in range(num-2):

            fib_seq.append(fib_seq[i] + fib_seq[i+1])

        fib_seq = list(map(int, fib_seq))
        print(fib_seq[-1] + fib_seq[-2])
fibonacci()

# num1, num2, num = 0, 1, int(input())
# for i in range(num):
#     result = num1 + num2
#     num1, num2 = num2, result
#     print(result)
