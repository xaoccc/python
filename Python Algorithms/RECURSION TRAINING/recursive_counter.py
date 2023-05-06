def recursive_counter(start, end):
    print(start) 
    if start == end:
        return
    else:
        recursive_counter(start + 1, end)
    
recursive_counter(int(input()), int(input())) 
