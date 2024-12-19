def find_longest_string(string_list):
    longest = ''
    for string in string_list:
        if len(string) > len(longest):
            longest = string
    return longest


longest = find_longest_string(['apple', 'banana', 'kiwi', 'pear'])
print(longest)

"""
    EXPECTED OUTPUT:
    ----------------
    banana

"""