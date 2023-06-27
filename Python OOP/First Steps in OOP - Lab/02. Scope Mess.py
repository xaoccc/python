
x = "global"
def outer():
    x = "local"
    def inner():
        # 5. We define a value of x which is also for outer()
        nonlocal x
        # 6. change the variable and print it -> inner: nonlocal
        x = "nonlocal"
        print("inner:", x)
    def change_global():
        # 9. Change the variable with the value of x outside the function(global)
        global x
        # 10. Add some text to it and print it
        x = x + ": changed!"
        print(x)
    
    # 3. print the variable defined at the beginning of outer()    
    print("outer:", x)
    # 4. Call the inner() funcion
    inner()
    # 7. x should be changed here by the function inner(), so the result should be "inner: nonlocal"
    print("outer:", x)
    # 8. Call the change_global() function 
    change_global()

# 1. print the global variable    
print(x)
# 2. Call the outer() function
outer()
