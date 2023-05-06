def concatenate(*some_text, **more_text):
    some_text = "".join(list(some_text))
    
    for key, value in more_text.items():
        if key in some_text:
            some_text = some_text.replace(key, value)

    return some_text
