def naughty_or_nice_list(fargs, *args, **kwargs):
    print(kwargs)
    total_kids = {}
    kids_filter = {}

    for kid in fargs:
        if kid[0] not in total_kids:
            total_kids[kid[0]] = []
        total_kids[kid[0]].append(kid[1])


    for i in args:
        i = i.split("-")
        if i[0] not in kids_filter:
            kids_filter[i[0]] = []
        kids_filter[i[0]].append(i[1])

    nice_naughty = {"Nice":[], "Naughty": [], "Not found":[]}

    for key, value in total_kids.items():
        if len(value) == 1:
            if key in kwargs:
                nice_naughty[kwargs[key]].append(value)
                print(nice_naughty)


            for i in args:
                if str(key) in i:
                    nice_naughty[i[1]].append(value[0])

        for kid_name_kwargs, nice_naughty_kwargs in kwargs.items():
            for kid_name in value:
                if kid_name == kid_name_kwargs:
                    nice_naughty[nice_naughty_kwargs].append(kid_name)

    return kids_filter


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))