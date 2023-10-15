from copy import deepcopy

cols, rows = [int(input()), int(input())]
playground = [[0 for j in range(cols)] for i in range(rows)]
reset_game = deepcopy(playground)
player_one_coords, player_two_coords = [], []
player_one_win, player_two_win = False, False

def out_of_playground(row, col):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return True
    return False

def win_check(player_win, n):
    if playground[j][k] == n:
        if k + 1 < cols and playground[j][k + 1] == n:
            if k + 2 < cols and playground[j][k + 2] == n:
                if k + 3 < cols and playground[j][k + 3] == n:
                    player_win = True
                elif j + 1 < rows and playground[j + 1][k + 2] == n:
                    player_win = True
                elif j > 0 and playground[j - 1][k + 2] == n:
                    player_win = True
            elif j + 1 < rows and playground[j + 1][k + 1] == n:
                if k + 1 < cols and playground[j + 1][k + 2] == n:
                    player_win = True
                elif j + 2 < rows and k + 1 < cols and playground[j + 2][k + 1] == n:
                    player_win = True
            elif j > 0 and playground[j - 1][k + 1] == n:
                if j + 1 < rows and playground[j + 1][k] == n:
                    player_win = True
                elif j > 1 and playground[j - 2][k + 1] == n:
                    player_win = True
                elif k + 2 < cols and playground[j - 1][k + 2] == n:
                    player_win = True

        elif k > 0 and playground[j][k - 1] == n:
            if k > 1 and playground[j][k - 2] == n:
                if k > 2 and playground[j][k - 3] == n:
                    player_win = True
                elif j + 1 < rows and playground[j + 1][k - 2] == n:
                    player_win = True
                elif j > 0 and playground[j - 1][k - 2] == n:
                    player_win = True
            elif j > 0 and playground[j - 1][k - 1] == n:
                if j > 1 and playground[j - 2][k - 1] == n:
                    player_win = True
                elif k > 1 and playground[j - 1][k - 2] == n:
                    player_win = True
            elif j + i < rows and playground[j + 1][k - 1] == n:
                if playground[j + 1][k] == n:
                    player_win = True
                elif j + 2 < rows and playground[j + 2][k - 1] == n:
                    player_win = True
                elif k > 1 and playground[j + 1][k - 2] == n:
                    player_win = True

        elif j + 1 < rows and playground[j + 1][k] == n:
            if j + 2 < rows and playground[j + 2][k] == n:
                if j + 3 < rows and playground[j + 3][k] == n:
                    player_win = True
                elif k + 1 < cols and playground[j + 2][k + 1] == n:
                    player_win = True
                elif k > 0 and playground[j + 2][k - 1] == n:
                    player_win = True
            elif k + 1 < cols and playground[j + 1][k + 1] == n:
                if k + 2 < cols and playground[j + 1][k + 2] == n:
                    player_win = True
                elif j + 2 < rows and playground[j + 2][k + 1] == n:
                    player_win = True
            elif k > 0 and playground[j + 1][k - 1] == n:
                if playground[j][k - 1] == n:
                    player_win = True
                elif k > 1 and playground[j + 1][k - 2] == n:
                    player_win = True
                elif j + 2 < rows and playground[j + 2][k - 1] == n:
                    player_win = True

        elif j > 0 and playground[j - 1][k] == n:
            if j > 1 and playground[j - 2][k] == n:
                if j > 2 and playground[j - 3][k] == n:
                    player_win = True
                elif k + 1 < cols and playground[j - 2][k + 1] == n:
                    player_win = True
                elif k > 0 and playground[j - 2][k - 1] == n:
                    player_win = True
            elif k + 1 < cols and playground[j - 1][k + 1] == n:
                if playground[j][k + 1] == n:
                    player_win = True
                elif k + 2 < cols and playground[j - 1][k + 2] == n:
                    player_win = True
                elif j > 1 and playground[j - 2][k + 1] == n:
                    player_win = True
            elif k > 0 and playground[j - 1][k - 1] == n:
                if playground[j][k - 1] == n:
                    player_win = True
                elif k > 1 and playground[j - 1][k - 2] == n:
                    player_win = True
                elif j > 1 and playground[j - 2][k - 1] == n:
                    player_win = True
    if player_win == True: 
        return True

i = 0
while True:
    i += 1
    coords = [int(i) for i in input().split()]
    row = coords[0]
    col = coords[1]
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
                if win_check(player_one_win, 1):
                    print("Player one wins!")
                    new_game = input("Do you want an new game? y/n:")
                    print(new_game)
                    if new_game == "y":
                        playground = reset_game
                        break
                    elif new_game == "n":
                        raise SystemExit("Good game!")
                    else:
                        while new_game != "y" and new_game != "n":
                            print("Invalid input!")
                            new_game = input("Do you want an new game? y/n:")
                        if new_game == "y":
                            playground = reset_game
                            break
                        elif game == "n":
                            raise SystemExit("Good game!")
                        
                    break
                elif win_check(player_two_win, 2):
                    print("Player two wins!")
                    new_game = input("Do you want an new game? y/n:")
                    print(new_game)
                    if new_game == "y":
                        playground = reset_game
                        break
                    elif new_game == "n":
                        raise SystemExit("Good game!")
                    else:
                        while new_game != "y" and new_game != "n":
                            print("Invalid input!")
                            new_game = input("Do you want an new game? y/n:")
                        if new_game == "y":
                            playground = reset_game
                            break
                        elif new_game == "n":
                            raise SystemExit("Good game!")
                
                if playground == reset_game:
                    break
            if playground == reset_game:
                i = 0
                player_one_coords, player_two_coords = [], []
                player_one_win, player_two_win = False, False
                break

    for row in playground:
        print(*row, sep="|")
