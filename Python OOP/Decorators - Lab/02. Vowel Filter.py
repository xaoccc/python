def vowel_filter(function):
    def wrapper():
        vowels = ["a", "e", "o", "i", "u", "y"]
        return [i for i in function() if i in vowels]
    return wrapper
