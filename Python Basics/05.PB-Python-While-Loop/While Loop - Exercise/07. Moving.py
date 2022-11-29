space_width = int(input())
space_lenght = int(input())
space_height = int(input())
boxes_capacity = space_width * space_lenght * space_height
boxes_total = 0

while boxes_capacity > boxes_total:
    boxes_moved = input()
    if boxes_moved == "Done":
        print(f"{boxes_capacity - boxes_total} Cubic meters left.")
        break
    boxes_total += int(boxes_moved)
else:
    print(f"No more free space! You need {boxes_total - boxes_capacity} Cubic meters more.")