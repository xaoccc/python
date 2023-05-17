def forecast(*args):
    weather = ["Sunny", "Rainy", "Cloudy"]
    result = ""
    args = dict(sorted(args, key=lambda x: (x[1]==weather[1], x[1]==weather[2], x[1]==weather[0], x[0])))
    for city, weather in args.items():
        result += f"{city} - {weather}\n"
    return result
