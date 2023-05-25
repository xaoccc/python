import copy

def naughty_or_nice_list(fargs, *args, **kwargs):
    santa_list = {}
    kids_filter = {}
    all_kids_in_santa_list = []
    result = ""
    
    for kid in fargs:
        if kid[0] not in santa_list:
            santa_list[kid[0]] = []
        santa_list[kid[0]].append(kid[1])

    for i in args:
        i = i.split("-")
        kids_filter[int(i[0])] = i[1]
    
    nice_naughty = {"Nice":[], "Naughty": [], "Not found":[]}
    for kid in santa_list.values():
        all_kids_in_santa_list += kid
    
    for number, kids_names in copy.deepcopy(santa_list).items():
        if len(kids_names) == 1:
            if number in kids_filter:
                nice_naughty[kids_filter[number]].append(kids_names[0])
                santa_list.pop(number)        
    
              
    for number, kids_names in copy.deepcopy(santa_list).items():
        for kid in kids_names:
            if all_kids_in_santa_list.count(kid) == 1 and number in kids_filter:
                nice_naughty[kwargs[kid]].append(kid)
        if number in kids_filter:
            santa_list.pop(number)
            
    if santa_list:
        for number, kids_names in santa_list.items():
            for kid in kids_names:
                nice_naughty["Not found"].append(kid)

    for key, names in nice_naughty.items():
        if names:
            result += f"{key}: {', '.join(names)}\n"

    return result
