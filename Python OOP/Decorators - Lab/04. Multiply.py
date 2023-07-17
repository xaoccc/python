def multiply(function):
    def decorator(number):
        def wrapper(params):
            return number(params) * function
        return wrapper
    return decorator
