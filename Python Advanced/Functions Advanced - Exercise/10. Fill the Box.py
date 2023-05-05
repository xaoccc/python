def fill_the_box(*arg):
    box_capacity = arg[0] * arg[1] * arg[2]
    i = 3
    while arg[i] != "Finish":
        box_capacity -= arg[i]
        i += 1
    if box_capacity > 0:
        return f"There is free space in the box. You could put {box_capacity} more cubes."
    else:
        return f"No more free space! You have {abs(box_capacity)} more cubes."
