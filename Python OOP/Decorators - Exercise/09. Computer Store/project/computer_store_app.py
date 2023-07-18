from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0
        
    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_computers = { "Desktop Computer": DesktopComputer, "Laptop": Laptop}
        if type_computer not in valid_computers:
            raise ValueError(f"{ type_computer } is not a valid type computer!")
        computer = valid_computers[type_computer](manufacturer, model)
        self.warehouse.append(computer)
        return computer.configure_computer(processor, ram)
        
    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.processor == wanted_processor and computer.ram >= wanted_ram and client_budget >= computer.price:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for { client_budget }$."
        raise Exception("Sorry, we don't have a computer for you.")