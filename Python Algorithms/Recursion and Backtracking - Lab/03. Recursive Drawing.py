num = int(input())

def draw(num):
    if num == 0:
        return
    print("*" * num)    
    draw(num - 1)
    print("#" * num)
    
draw(num)
