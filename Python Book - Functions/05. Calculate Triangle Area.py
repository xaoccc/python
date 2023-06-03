def get_triangle_area(a, h):
    if int((a * h) / 2) == (a * h) / 2:
        return int((a * h) / 2)
    else:
        return (a * h) / 2
        
a =  float(input())   
h =  float(input())   
print(get_triangle_area(a, h))
