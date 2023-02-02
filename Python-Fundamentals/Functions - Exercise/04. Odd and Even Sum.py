def odd_even_sum(num):

    def odd_sum_funk():
        odd_sum = 0
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                odd_sum += int(num[i])
        print(f"Odd sum = {odd_sum}, ", end="")
    odd_sum_funk()
    
    def even_sum_funk():
        even_sum = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                even_sum += int(num[i])
        print(f"Even sum = {even_sum}")
    even_sum_funk()
    
odd_even_sum(input())
