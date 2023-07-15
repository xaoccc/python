from itertools import permutations


def possible_permutations(nums):
    for i in list(permutations(nums)):
        yield list(i)

