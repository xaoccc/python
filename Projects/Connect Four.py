cols, rows = [int(input()), int(input())]
playground = [[0 for j in range(cols)] for i in range(rows)]
player_one_coords, player_two_coords = [], []
player_one_win, player_two_win = False, False

directions = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

def out_of_playground(row, col):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return True
    return False


i = 0
while True:
    i += 1
    player_one, player_two = 0, 0
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
                if playground[j][k] == 1:
                    if k + 1 < cols and playground[j][k + 1] == 1:
                        if k + 2 < cols and playground[j][k + 2] == 1:
                            if k + 3 < cols and playground[j][k + 3] == 1:
                                player_one_win = True
                            elif k + 2 < cols and j + 1 < rows and playground[j + 1][k + 2] == 1:
                                player_one_win = True
                            elif k + 2 < cols and j > 0 and playground[j - 1][k + 2] == 1:
                                player_one_win = True
                        elif k + 1 < cols and j + 1 < rows and playground[j + 1][k + 1] == 1:
                            if k + 1 < cols and j + 1 < rows and playground[j + 1][k + 2] == 1:
                                player_one_win = True
                            elif j + 2 < rows and k + 1 < cols and playground[j + 2][k + 1] == 1:
                                player_one_win = True
                        elif j > 0 and k + 1 < cols and playground[j - 1][k + 1] == 1:
                            if j + 1 < rows and playground[j + 1][k] == 1:
                                player_one_win = True
                            elif j > 1 and k + 1 < cols and playground[j - 2][k + 1] == 1:
                                player_one_win = True
                            elif j > 0 and k + 2 < cols and playground[j - 1][k + 2] == 1:
                                player_one_win = True

                    elif k > 0 and playground[j][k - 1] == 1:
                        if k > 1 and playground[j][k - 2] == 1:
                            if k > 2 and playground[j][k - 3] == 1:
                                player_one_win = True
                            elif j + 1 < rows and playground[j + 1][k - 2] == 1:
                                player_one_win = True
                            elif j > 0 and playground[j - 1][k - 2] == 1:
                                player_one_win = True
                        elif j > 0 and playground[j - 1][k - 1] == 1:
                            if j > 1 and playground[j - 2][k - 1] == 1:
                                player_one_win = True
                            elif k > 1 and playground[j - 1][k - 2] == 1:
                                player_one_win = True
                        elif j + i < rows and playground[j + 1][k - 1] == 1:
                            if playground[j + 1][k] == 1:
                                player_one_win = True
                            elif j + 2 < rows and playground[j + 2][k - 1] == 1:
                                player_one_win = True
                            elif k > 1 and playground[j + 1][k - 2] == 1:
                                player_one_win = True

                    elif j + 1 < rows and playground[j + 1][k] == 1:
                        if j + 2 < rows and playground[j + 2][k] == 1:
                            if j + 3 < rows and playground[j + 3][k] == 1:
                                player_one_win = True
                            elif k + 1 < cols and playground[j + 2][k + 1] == 1:
                                player_one_win = True
                            elif k > 0 and playground[j + 2][k - 1] == 1:
                                player_one_win = True
                        elif k + 1 < cols and playground[j + 1][k + 1] == 1:
                            if k + 2 < cols and playground[j + 1][k + 2] == 1:
                                player_one_win = True
                            elif j + 2 < rows and playground[j + 2][k + 1] == 1:
                                player_one_win = True
                        elif k > 0 and playground[j + 1][k - 1] == 1:
                            if playground[j][k - 1] == 1:
                                player_one_win = True
                            elif k > 1 and playground[j + 1][k - 2] == 1:
                                player_one_win = True
                            elif j + 2 < rows and playground[j + 2][k - 1] == 1:
                                player_one_win = True

                    elif j > 0 and playground[j - 1][k] == 1:
                        if j > 1 and playground[j - 2][k] == 1:
                            if j > 2 and playground[j - 3][k] == 1:
                                player_one_win = True
                            elif k + 1 < cols and playground[j - 2][k + 1] == 1:
                                player_one_win = True
                            elif k > 0 and playground[j - 2][k - 1] == 1:
                                player_one_win = True
                        elif k + 1 < cols and playground[j - 1][k + 1] == 1:
                            if playground[j][k + 1] == 1:
                                player_one_win = True
                            elif k + 2 < cols and playground[j - 1][k + 2] == 1:
                                player_one_win = True
                            elif j > 1 and playground[j - 2][k + 1] == 1:
                                player_one_win = True
                        elif k > 0 and playground[j - 1][k - 1] == 1:
                            if playground[j][k - 1] == 1:
                                player_one_win = True
                            elif k > 1 and playground[j - 1][k - 2] == 1:
                                player_one_win = True
                            elif j > 1 and playground[j - 2][k - 1] == 1:
                                player_one_win = True

        if player_one_win:
            print("Player one wins!")
        elif player_two_win:
            print("Player two wins!")

    for row in playground:
        print(*row)
