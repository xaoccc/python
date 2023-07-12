class countdown_iterator:
    def __init__(self, start):
        self.start = start
        self.end = 0        

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            value = self.start
            self.start -= 1
            return value
        else:
            raise StopIteration
