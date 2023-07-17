def cache():
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


# TODO: Implement

@cache()
def fibonacci(n):
    log1 = {}
    if n not in log1:
        if n < 2:
            log1[n] = n
            return n
        else:
            log1[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return fibonacci(n - 1) + fibonacci(n - 2)

    def log(log1):
        return log1




print(fibonacci(3))
print(fibonacci.log)

