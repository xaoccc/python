expression = [int(i) if i.isnumeric() or i.lstrip("-").isdigit() else i for i in input().split()]
current = []
result = 0
for i in range(len(expression)):
    if type(expression[i]) == int:
        current.append(expression[i])
    else:
        if expression[i] == "-":
            result = current[0]
            for num in range(1, len(current)):
                result -= current[num]
            current = [result]
        elif expression[i] == "+":
            result = current[0]
            for num in range(1, len(current)):
                result += current[num]
            current = [result]
        elif expression[i] == "*":
            result = current[0]
            for num in range(1, len(current)):
                result *= current[num]
            current = [result]
        elif expression[i] == "/":
            result = current[0]
            for num in range(1, len(current)):
                result //= current[num]
            current = [result]
        
print(result)
