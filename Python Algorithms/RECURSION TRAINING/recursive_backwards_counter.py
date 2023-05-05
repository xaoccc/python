def recursive_backwards_counter(end, start):
    print(end) 
    if start == end:
        return
    else:
       recursive_backwards_counter(end - 1, start)
    
recursive_backwards_counter(int(input()), int(input()))
