def flights(*args):
    all_flights = {}
    i = 0
    while args[i] != "Finish":
        if type(args[i]) is str:
            if args[i] not in all_flights:
                all_flights[args[i]] = 0
        else:
            all_flights[args[i - 1]] += args[i]
        i += 1

    return all_flights
