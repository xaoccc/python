x = "global"
def outer():
    x = "local"
    def inner():
        
        x = "nonlocal"
        print("inner:", x)
    def change_global():
        x = "global: changed!"
        print(x)
        
    print("outer:", x)
    x = "nonlocal"
    inner()
    print("outer:", x)
    change_global()

    
print(x)
outer()
