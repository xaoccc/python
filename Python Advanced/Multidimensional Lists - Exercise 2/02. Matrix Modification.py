matrix_size = int(input())
matrix = [[int(j) for j in input().split()] for i in range(matrix_size)]
command = input()
while command != "END":
    command = [int(i) if i.isdigit() or "-" in i else i for i in command.split()]
    
    if 0 > command[1] or command[1] >= matrix_size or 0 > command[2] or command[2] >= matrix_size:
        print("Invalid coordinates")
    elif command[0] == "Add":
        matrix[command[1]][command[2]] += command[3]
    elif command[0] == "Subtract":
        matrix[command[1]][command[2]] -= command[3]
        
    command = input()
for i in matrix:
    print(*i)
