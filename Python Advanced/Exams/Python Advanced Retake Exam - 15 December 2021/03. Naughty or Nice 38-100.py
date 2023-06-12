def naughty_or_nice_list(kids, *args, **kwargs):
    santa_list = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    kids_dict = {}
    kids_dict_reversed = {}
    result = ""
    
    for kid in kids:
        if kid[0] not in kids_dict:
            kids_dict[kid[0]] = []
        kids_dict[kid[0]].append(kid[1])
    
    
    if args:
        for i in args:
            current = [int(i) if i.isdigit() else i for i in i.split("-")]
            if current[0] in kids_dict:
                if len(kids_dict[current[0]]) == 1:
                    santa_list[current[1]].append(kids_dict[current[0]][0])
                    for kid in kids:
                        if kid[0] == current[0] and kid[1] == kids_dict[current[0]][0]:
                            kids.remove(kid)
                    
    for kid in kids:
        if kid[1] not in kids_dict_reversed:
            kids_dict_reversed[kid[1]] = []
        kids_dict_reversed[kid[1]].append(kid[0])                
        
    if kwargs:
        for key, value in kwargs.items():
            if key in kids_dict_reversed:
                if len(kids_dict_reversed[key]) == 1:
                    santa_list[value].append(key)
                    for kid in kids:
                        if kids_dict_reversed[key][0] == kid[0] and kid[1] == key:
                            kids.remove(kid)
    
    if kids:        
        for kid in kids:
            santa_list["Not found"].append(kid[1])
    for key, value in santa_list.items():
        if value:
            result += f"{key}: {', '.join(value)}\n"
    return result
