class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.space_left = 0

    def add_item(self, item: str):
        
        if self.__capacity > self.space_left:
            self.space_left += 1
            self.items.append(str(item))
        else:
            return "not enough room in the inventory"
            
    def get_capacity(self):
        return self.__capacity
        
    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.get_capacity(self) - self.space_left}"
        
inventory = Inventory(2)
inventory.add_item("Car")
print(inventory.get_capacity())
inventory.add_item("Bike") 
print(inventory.get_capacity())
print(inventory.add_item("bottle"))
print(inventory)
