from time import sleep

def mark(darts, row, col):
    
    if row < 0 or row > 6 or col < 0 or col > 6:
        return
    
    if darts[row][col] != "current_color":
        return
    
    if darts[row][col] == "current_color":
        darts[row][col] = "red"

    mark(darts, row - 1, col)
    mark(darts, row, col - 1)
    mark(darts, row + 1, col)
    mark(darts, row, col + 1)
    #some logic for adding to total score...
    return darts

def unmark(darts, row, col):
    
    if row < 0 or row > 6 or col < 0 or col > 6:
        return
    
    if darts[row][col] != "red":
        return
    
    if darts[row][col] == "red":
        darts[row][col] = "random_color_generated_with_randint"

    unmark(darts, row - 1, col)
    unmark(darts, row, col - 1)
    unmark(darts, row + 1, col)
    unmark(darts, row, col + 1)
    
    return darts
  
 if hit_sector == "current_color":
        mark(darts, throw[0], throw[1])
        for row in darts:
            print(*row)
        sleep(3)
        unmark(darts, throw[0], throw[1])
        for row in darts:
            print(*row)
