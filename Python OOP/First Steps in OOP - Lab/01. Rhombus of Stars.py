def print_stars(size, star_count):
    # on first iteration star_count==1:
    # if size==1, we print just " "
    # if size==2, we print  " "*2...
    # So until the end of loop1 the size of " " decreases until reaches 0, the opposite happens in loop2
    for i in range(size - star_count):
        print(" ", end="")
    # if size==1, we print just "* "
    # if size==2, we print  "* "*2...
    # So until the end of loop1 the size of "* " increases until reaches size-1, e.g. 2 if size==3 , the opposite happens in loop2
    for i in range(1, star_count):
        print("*", end=" ")
    #we always add "*", otherwise the size has height/lenght size-1
    print("*")

size = int(input())
# loop1 - print first half
for star_count in range(1, size):
    print_stars(size, star_count)
# loop2 - print second half
for star_count in range(size, 0, -1):
    print_stars(size, star_count)
    
    
# todo: def print_rhombus(n)
