class MyContext:
    def __enter__(self):
        for num in range(3):
            print(num)
        print("Entering the block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        for num in range(7, 10):
            print(num)
        print("Exiting the block")


with MyContext() as ctx:
    for num in range(4, 7):
        print(num)
    print("Inside the block")
