def make_bold(function):
    def wrapper(*text):
        return f"<b>{function(*text)}</b>"
    return wrapper
    
def make_italic(function):
    def wrapper(*text):
        return f"<i>{function(*text)}</i>"
    return wrapper
    
def make_underline(function):
    def wrapper(*text):
        return f"<u>{function(*text)}</u>"
    return wrapper
