from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
        
    @staticmethod
    def dvd_capacity():
        return 15
        
    @staticmethod    
    def customer_capacity():
        return 10
        
    def add_customer(self, customer):
        if self.customer_capacity() - len(self.customers) and customer not in self.customers:
            self.customers.append(customer)
            
    def add_dvd(self, dvd):
        if self.dvd_capacity() - len(self.dvds) and dvd not in self.dvds:
            self.dvds.append(dvd)
            
    def rent_dvd(self, customer_id, dvd_id):
        current_dvd, current_customer = None, None
        
        for dvd in self.dvds: 
            if dvd.id == dvd_id:
                current_dvd = dvd
        
        for customer in self.customers:
            if customer.id == customer_id:
                if current_dvd in customer.rented_dvds:
                    return f"{customer.name} has already rented {current_dvd.name}"
                if current_dvd and customer.age < current_dvd.age_restriction:
                    return f"{customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
                current_customer = customer
        
        if current_dvd and current_dvd.is_rented:
            return "DVD is already rented"
            
        if current_customer and current_dvd:
            current_dvd.is_rented = True
            current_customer.rented_dvds.append(current_dvd)
            return f"{current_customer.name} has successfully rented {current_dvd.name}"
            
    def return_dvd(self, customer_id, dvd_id):
        current_dvd, current_customer = None, None
        for dvd in self.dvds: 
            if dvd.id == dvd_id:
                current_dvd = dvd
                
        for customer in self.customers:
            if customer.id == customer_id:
                if current_dvd in customer.rented_dvds:
                    customer.rented_dvds.remove(current_dvd)
                    current_dvd.is_rented = False
                    return f"{customer.name} has successfully returned {current_dvd.name}"
                current_customer = customer
        
        return f"{current_customer.name} does not have that DVD"
        
    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{str(customer)}\n"
        for dvd in self.dvds:
            result += f"{str(dvd)}\n"
        result = result.strip()
        return result