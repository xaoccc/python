class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.tries = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.tries < self.count:
            value = self.start
            self.start += self.step
            self.tries += 1
            return value
        else:
            raise StopIteration
