class Inventory:

    def __init__(self, capacity: int):
        self.items = []
        self.__capacity = capacity
        
    def add_item(self, item: str):
        if self.__capacity > 0:
            self.__capacity -= 1
            self.items.append(str(item))
        else:
            return "not enough room in the inventory"
            
    def get_capacity(self):
        return self.__capacity
        
    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"
        
inventory = Inventory(2)
inventory.add_item("Car")
print(inventory.get_capacity())
inventory.add_item("Bike") 
print(inventory.get_capacity())
print(inventory.add_item("bottle"))
print(inventory)