class MyContext:
    def __enter__(self):
        print("Start event loop")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End event loop")


with MyContext() as ctx:
    print("Processing message")
