def nested_loops(idx, result):
    # Bottom of recursion. We return/print result here.
    if idx >= num:
        print(" ".join([str(i) for i in result]))
        return
    else:
        for i in range(1, num+1):
            result[idx] = i
            nested_loops(idx + 1, result)


num = int(input())
result = [0] * num

nested_loops(0, result)