def func_executor(*funcs):
    result = []
    
    for j in range(len(funcs)):
        args_func = []
        for i in range(len(funcs[j][1])):
            args_func.append(funcs[j][1][i])        
        result.append(f"{funcs[j][0].__name__} - {funcs[j][0](*args_func)}\n")

    return "".join([str(i) for i in result])
