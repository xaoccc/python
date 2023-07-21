from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth

class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0
        
    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacies = {"Gingerbread": Gingerbread, "Stolen": Stolen}
        
        if type_delicacy not in delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
            
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")
        
        self.delicacies.append(delicacies[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
        
    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booths = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}
        
        if type_booth not in booths:
            raise Exception(f"{type_booth} is not a valid booth!")
            
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")
        
        self.booths.append(booths[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."
        
    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.is_reserved = True
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")
        
    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_booth, current_delicacy = "", ""
        
        for booth in self.booths:
            if booth.booth_number == booth_number:
                current_booth = booth
                break
            
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                current_delicacy = delicacy
                break
        
        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")
            
        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
            
        current_booth.delicacy_orders.append(current_delicacy)    
        return f"Booth {booth_number} ordered {delicacy_name}."
        
    def leave_booth(self, booth_number: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                this_booth_income = 0
                for order in booth.delicacy_orders:
                    this_booth_income += order.price
                this_booth_income += booth.price_for_reservation
                booth.price_for_reservation = 0
                booth.is_reserved = False
                booth.delicacy_orders = []
                break

        self.income += this_booth_income
        return f"Booth {booth_number}:\nBill: {this_booth_income:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
