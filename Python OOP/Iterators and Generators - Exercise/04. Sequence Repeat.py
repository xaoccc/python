class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = -1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.sequence) - 1:
            self.idx = -1
        if self.counter == self.number:
            raise StopIteration
        self.counter += 1
        self.idx += 1
        return self.sequence[self.idx]

