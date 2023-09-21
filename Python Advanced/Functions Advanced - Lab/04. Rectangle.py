def rectangle(*size):
    if int(size[0]) == size[0] and int(size[1]) == size[1]:
        def area():
            return size[0] * size[1]

        def perimeter():
            return sum(size) * 2

        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return "Enter valid values!"
        
# test: print(rectangle(2, 10)) 
