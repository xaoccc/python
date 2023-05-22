def start_spring(**kwargs):
    spring_data = {}
    result = ""    
    for key, value in kwargs.items():
        if value not in spring_data:
            spring_data[value] = []
        spring_data[value].append(key)
    for key in spring_data.keys():
        spring_data[key] = sorted(spring_data[key])
    spring_data = dict(sorted(spring_data.items(), key=lambda x: (-len(x[1]), x[0], x[1])))
    
    for key, value in spring_data.items():
        result += f"{key}:\n"
        for i in value:
            result += f"-{i}\n"
    
    return result
