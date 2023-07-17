def logged(function):
    def wrapper(*args):
        return f"you called {function.__name__}{args}\nit returned {function(*args)}"
    return wrapper
