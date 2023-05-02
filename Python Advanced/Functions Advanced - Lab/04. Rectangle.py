def rectangle(*size):
    result = []
    if int(size[0]) == size[0] and int(size[1]) == size[1]:
        def area(size):
            return size[0] * size[1]
        result.append((area(size))) 
        
        def perimeter(size):
            return sum(size) * 2
        result.append((perimeter(size)))
        return f"Rectangle area: {result[0]}\nRectangle perimeter: {result[1]}"
    else:
        return "Enter valid values!"
        
# test: print(rectangle(2, 10)) 
