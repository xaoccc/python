def even_parameters(function):
    def wrapper(*args):
        if not args:
            return function()
        result = sum([i if type(i) == int and i % 2 == 0 else 3.1456 for i in args])
        return result if type(result) != float else "Please use only even numbers!"
    return wrapper
