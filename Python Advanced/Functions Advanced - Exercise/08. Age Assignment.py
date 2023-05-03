def age_assignment(*args, **kwargs):
    i = 0
    result = ""
    result_dict = {}
    for j in list(args):
        for name, age in kwargs.items():
            if j[0] == name[0]:
                name = j
                result_dict[name] = str(age)  
    result_dict = dict(sorted(result_dict.items(), key=lambda x: x[0]))    
    for name, age in  result_dict.items():    
        result += f"{name} is {age} years old.\n"
        i += 1
    return result
