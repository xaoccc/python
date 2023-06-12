def numbers_searching(*args):
    full_list, result = [], []
    for i in range(min(args), max(args) + 1):
        full_list.append(i)
    result.append(list(set(full_list) - set(args))[0])    
    result.append(sorted(list(set([i for i in args if args.count(i) > 1]))))
        
    return result
