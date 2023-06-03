def integer_to_base(number, base):
    result = ""
    while number != 0:
        result += str( number % base)
        number //= base
    print(result[::-1])
        
    
integer_to_base(int(input()), int(input()))
