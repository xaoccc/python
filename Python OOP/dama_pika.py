#This is a decorator with name "ritual" with an argument func
def ritual(func):
  # In it we wrap all code as it takes all provided arguments
    def wrapper(*args, **kwargs):
      # Call the function three times, as it also takes all possible arguments
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

# Pass data into the decorator, so that the result of dama_pika(name) == func  
@ritual
def dama_pika(name):
    print(f"{name}")

# Call the decorated function    
dama_pika("Dama Pika!")




def ritual(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        # If we dont return here,  dama_pika(name) will also not return any value, just print 3 times Dama Pika!!!!
        # In this case, we return the argument given  - dama_pika("Dama Pika!") and print it as well
        return func(*args, **kwargs)
    return wrapper

@ritual
def dama_pika(name):
    print("Dama Pika!!!!")
    return f"{name}"
    
test = dama_pika("Dama Pika!")
print(test)

# Output:
# Dama Pika!!!!
# Dama Pika!!!!
# Dama Pika!!!!
# Dama Pika!
