N1 = int(input())
N2 = int(input())
operator = input()

result = 0
output = ""

if N2 == 0 and (operator == "/" or operator =="%"):
    output = f"Cannot divide {N1} by zero"
    
elif operator == "/" :
    result = N1 / N2
    output = f"{N1} {operator} {N2} = {result:.2f}"
    
elif operator == "%" :
    result = N1 % N2
    output = f"{N1} {operator} {N2} = {result}"

else :
    if operator == "+" :
        result = N1 + N2
    elif operator == "-" :
        result = N1 - N2 
    elif operator == "*" :
        result = N1 * N2
    output = f"{N1} {operator} {N2} = {result} " f"- {('even' if result % 2 == 0 else 'odd')}"
    
print (output)