rows, cols = [int(i) for i in input().split()]
matrix = []

for row in range(rows):
    current_row = input().split()
    if len(current_row) != cols:
        print("Invalid input!")
    else:
        matrix.append(current_row)
    
command = input()    
while command != "END":
    command = [int(i) if i.isdigit() else i for i in command.split() ]
    if len(command) != 5 or command[0] != "swap" or command[1] < 0 or command[1] > rows - 1 or command[3] < 0 or command[3] > rows - 1 or command[2] < 0 or command[2] > cols - 1 or command[4] < 0 or command[4] > cols - 1:
        print("Invalid input!")
    else:
        matrix[command[1]][command[2]], matrix[command[3]][command[4]] = matrix[command[3]][command[4]], matrix[command[1]][command[2]]
        for row in matrix:
            print(*row)
    command = input()
