from collections import deque

def best_list_pureness(*args):
    nums_list = deque(args[0])
    k = args[1]
    rotation, max_pureness, rotation_max_pureness = 0, 0, 0
    for i in range(k + 1):

        pureness = 0
        for j in range(len(nums_list)):
            pureness += nums_list[j] * j
            
        if pureness > max_pureness:
            max_pureness = pureness
            rotation_max_pureness = rotation
        nums_list.rotate(1)
        rotation += 1

    return f"Best pureness {max_pureness} after {rotation_max_pureness} rotations"  
