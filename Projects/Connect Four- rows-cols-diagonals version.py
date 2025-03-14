cols, rows = [int(input()), int(input())]
playground = [[0 for j in range(cols)] for i in range(rows)]
player_one_coords, player_two_coords = [], []
player = ""

def out_of_playground(row, col):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return True
    return False

def win_check(n):
    player_win_row, player_win_col, player_win_diag = False, False, False
    if playground[j][k] == n and j + 3 < rows and k + 3 < cols:
        player_win_diag = True
        for r in range(4):
            if playground[j + r][k + r] != n:
                player_win_diag = False
                break
            
    if playground[j][k] == n and j + 3 < rows:
        player_win_row = True
        for r in range(j, j + 4):
            if playground[r][k] != n:
                player_win_row = False
                break
    
    if playground[j][k] == n and k + 3 < cols:
        player_win_col = True
        for r in range(k, k + 4):
            if playground[j][r] != n:
                player_win_col = False
                break

    if player_win_row == True or player_win_col == True or player_win_diag == True: 
        return True

i = 0
while True:
    reset_game = False
    i += 1
    if i % 2 != 0: 
        player = "one"
    else:
        player = "two"
        
    row = int(input(f"Player {player} choose a row: "))
    col = int(input(f"Player {player} choose a column: "))
    coords = [row, col]
    
    if out_of_playground(row, col) or coords in player_one_coords or coords in player_two_coords:
        print("Invalid coordinates!")
        continue
    else:
        if i % 2 != 0:
            player_one_coords.append(coords)
            playground[row][col] += 1

        else:
            player_two_coords.append(coords)
            playground[row][col] += 2

        for j in range(rows):
            for k in range(cols):
                if win_check(1):
                    print("Player one wins!")
                    new_game = input("Do you want new game? y/n:")
                    print(new_game)
                    if new_game == "y":
                        reset_game = True
                        playground = [[0 for j in range(cols)] for i in range(rows)]
                        i = 0
                        player_one_coords, player_two_coords = [], []
                        break
                    elif new_game == "n":
                        raise SystemExit("Good game!")
                    else:
                        while new_game != "y" and new_game != "n":
                            print("Invalid input!")
                            new_game = input("Do you want new game? y/n:")
                        if new_game == "y":
                            reset_game = True
                            playground = [[0 for j in range(cols)] for i in range(rows)]
                            i = 0
                            player_one_coords, player_two_coords = [], []
                            break
                        elif game == "n":
                            raise SystemExit("Good game!")
                        
                    break
                elif win_check(2):
                    print("Player two wins!")
                    new_game = input("Do you want new game? y/n:")
                    print(new_game)
                    if new_game == "y":
                        reset_game = True
                        playground = [[0 for j in range(cols)] for i in range(rows)]
                        i = 0
                        player_one_coords, player_two_coords = [], []
                        break
                    elif new_game == "n":
                        raise SystemExit("Good game!")
                    else:
                        while new_game != "y" and new_game != "n":
                            print("Invalid input!")
                            new_game = input("Do you want new game? y/n:")
                        if new_game == "y":
                            reset_game = True
                            playground = [[0 for j in range(cols)] for i in range(rows)]
                            i = 0
                            player_one_coords, player_two_coords = [], []
                            break
                        elif new_game == "n":
                            raise SystemExit("Good game!")
                
                if reset_game:
                    break
            if reset_game:
                break

    for row in playground:
        print(*row, sep="|")
