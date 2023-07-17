def multiply(function):
    def decorator(number):
        def wrapper(*args, **kwargs):
            return number(*args, **kwargs) * function
        return wrapper
    return decorator
