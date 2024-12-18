
counter = 0
memo = [None] * 21
def fib(num):
    global counter
    counter += 1

    # We check if we have already called the function with this parameter (num),
    # If so, we return the value stored in the memo table instead of calling if again
    # This is reducing the number of function calls from 21891 to 39 for num = 20, progressively becoming more efficient as num increases
    if memo[num] is not None:
        return memo[num]

    if num == 1 or num == 0:
        memo[num] = num
        return num

    # Store each result of the recursive calls in the memo table
    memo[num] = fib(num - 1) + fib(num - 2)
    return memo[num]




print(fib(20))
print(memo)
print('Number of calls:', counter)