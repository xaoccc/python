def even_odd_filter(**nums):
    result = {}
    if "even" in nums:
        result['even'] = list(filter(lambda x: x % 2 == 0, nums["even"]))
    if "odd" in nums:
        result['odd'] = list(filter(lambda x: x % 2 != 0, nums["odd"]))

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))
