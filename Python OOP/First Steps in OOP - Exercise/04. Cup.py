class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

        
    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

        
    def status(self):
        return self.size - self.quantity
