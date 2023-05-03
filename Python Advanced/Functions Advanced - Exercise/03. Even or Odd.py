def even_odd(*nums):
    result = {
        "even": list(filter(lambda x: x % 2 == 0, nums[:-1])),
        "odd": list(filter(lambda x: x % 2 != 0, nums[:-1]))
    }
    return result[nums[-1]]
