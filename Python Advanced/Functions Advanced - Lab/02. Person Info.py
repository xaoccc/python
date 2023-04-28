def get_info(**kwargs):
    values = []
    for key, value in kwargs.items():
        values.append(value)
    return f"This is {values[0]} from {values[1]} and he is {values[2]} years old"
