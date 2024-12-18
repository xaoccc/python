def find_max_min(numbers):
    max_num = -1000000
    min_num = 1000000
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

print( find_max_min([5, 5, 5]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)

"""