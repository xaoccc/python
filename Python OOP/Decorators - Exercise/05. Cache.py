def cache():
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = {}
            log[args] = func(*args, **kwargs)
            return log
        return wrapper
    return decorator


# TODO: Implement

@cache()
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



fibonacci(3)
# print(fibonacci.log)

