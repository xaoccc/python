def cache(func):
    # func = def fibonacci(n):... We pass it here as argument
    # *args, **kwargs - here we take n, but as a standard, we write *args, **kwargs to take all possible arguments
    # We can write wrapper(n) and it will work just fine
    def wrapper(*args, **kwargs):
        # args[0] is n, the number we want to take the fibonacci row
        # The trickiest part is here. We add the key-value pair to the dictionary.
        # But we return the current result from fibonacci(n):
        # return func(*args, **kwargs) == return fibonacci(n - 1) + fibonacci(n - 2)
        wrapper.log[args[0]] = func(*args, **kwargs)
        return func(*args, **kwargs)
    # We define the dictionary here as wrapper argument, then we can use it in the wrapper and add data into it
    wrapper.log = {}
    return wrapper
    
@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

