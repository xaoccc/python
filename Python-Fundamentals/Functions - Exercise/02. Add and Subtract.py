def add_and_subtract():

    def subtract(sum_num):
        res = sum_num - int(input())
        return res
    
    def sum_numbers(num_two):
        res = num_two + int(input())
        return res
    
    output = subtract(sum_numbers(int(input())))
    print(output)

add_and_subtract()
