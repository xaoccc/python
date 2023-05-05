def recursive_backwards_accelerating_counter(end, start):
    print(end) 
    if start >= end:
        return
    elif start < end - 100:
        recursive_backwards_accelerating_counter(end - 2, start)
    elif start < end - 70:
        recursive_backwards_accelerating_counter(end - 3, start)
    elif start < end - 40:
        recursive_backwards_accelerating_counter(end - 4, start)
    else:
        recursive_backwards_accelerating_counter(end - 5, start)
    
recursive_backwards_accelerating_counter(int(input()), int(input()))
