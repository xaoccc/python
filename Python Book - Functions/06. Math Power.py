def calculate_power(a, n):
    if int(a ** n) == a ** n:
        return int(a ** n) 
    else:
        return a ** n
        
a =  float(input())   
n =  float(input())   
print(calculate_power(a, n))
