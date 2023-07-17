def tags(function):
    def decoraor(text):
        def wrapper(*arg):
            start = f"<{function}>"
            end = f"</{function}>"
            return f"{start}{text(*arg)}{end}"
        return wrapper
    return decoraor
