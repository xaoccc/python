num = int(input())

def sum_num(num):
    if num == 1:
        return num
    return num * sum_num(num-1)
    
print(sum_num(num))
