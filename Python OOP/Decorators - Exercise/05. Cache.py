def cache(func):
    def wrapper(*args, **kwargs):
        wrapper.log[args[0]] = func(*args, **kwargs)
        return func(*args, **kwargs)
    wrapper.log = {}
    return wrapper
    
@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

