def grocery_store(**kwargs):
    kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = ""
    for product, quantity in kwargs.items():
        if product == list(kwargs.keys())[-1]:
            result += f"{product}: {str(quantity)}"
        else:
            result += f"{product}: {str(quantity)} \n"
    return result
