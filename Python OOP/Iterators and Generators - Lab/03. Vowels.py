class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.vowels = ["a","e","o","i","y","u"]
        

    def __iter__(self):
        return self

    def __next__(self):

        while self.start < len(self.text):
            char = self.text[self.start]
            self.start += 1
            if char.lower() in self.vowels:
                return char

        raise StopIteration
