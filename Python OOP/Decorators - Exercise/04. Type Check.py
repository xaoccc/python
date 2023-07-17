def type_check(function):
    def decorator(number):
        def wrapper(params):
            return number(params) if type(params) == function else "Bad Type"
        return wrapper
    return decorator
