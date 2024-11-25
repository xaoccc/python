def first_non_repeating_char(text):
    my_dict = {}
    for i in text:
        if i not in my_dict:
            my_dict[i] = 0
        my_dict[i] += 1
    for j in text:
        if my_dict[j] == 1:
            return j
    return









print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('potop') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""