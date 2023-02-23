class Vehicle:
    
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None
        
    def buy(self, money: int, owner: str):
        if self.price <= money and self.owner == None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif self.price > money:
            return "Sorry, not enough money"
        else:
            return "Car already sold"
    
    def sell(self):
        if self.owner == None:
            return "Vehicle has no owner"
        else:
            self.owner = None
            
    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
