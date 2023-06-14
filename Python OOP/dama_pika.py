#This is a decorator with name "ritual" with an argument func
def ritual(func):
  # In it we wrap all code as it takes all provided arguments
    def wrapper(*args, **kwargs):
      # Call the function three times, as it also takes all possible arguments
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

# Pass data into the decorator, so that dama_pika(name) == func  
@ritual
def dama_pika(name):
    print(f"{name}")

# Call the decorated function    
dama_pika("Dama Pika!")
