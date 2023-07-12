class  dictionary_iter:
    def __init__(self, dicti):
        self.dicti = dicti
        self.start = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.start < len(self.dicti):
            value = self.start
            self.start += 1
            return tuple(list(self.dicti.items())[value])
        else:
            raise StopIteration
