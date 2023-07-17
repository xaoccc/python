def vowel_filter(function):
    def wrapper():
        return [i for i in function() if i.lower() in "aeiouy"]
    return wrapper
