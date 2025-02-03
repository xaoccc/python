import csv


# Read data from a CSV file and put in into an object (Cars_db)
# From the object Cars_db we can create more csv files, excel files, etc.
csv_data = []

with open('.\python\Python OOP\Python OOP for data handling\cars.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_data.append(row)


class Car:
    def __init__(self, make, model, year, vin, color, mileage, fuel_consumption):
        self.make = make
        self.model = model
        self.vin = vin
        self.year = year
        self.color = color
        self.mileage = mileage  
        self.fuel_consumption = fuel_consumption   

    def __repr__(self):
        return f'{self.year}, {self.make}, {self.model}, {self.vin}, {self.color}, {self.mileage}, {self.fuel_consumption}'
    

class Cars_collection():
    def __init__(self):
        self.Cars = {}
        self.counter = 0
    def add_Mailcat_object(self, Car):
        self.counter += 1
        self.Cars[self.counter] = Car

class create_cars_db():
    def __init__(self):
        self.data = Cars_collection()
        for car in csv_data:
            self.data.add_Mailcat_object(Car(car[0], car[1], car[2], car[3], car[4], car[5], car[6], car[7]))

    def list_cars(self):
        for car in self.data.Cars.values():
            print(car)

    def serialize_cars(self):
        response = []
        header = ["Make", "Model", "Year", "VIN", "Color", "Mileage", "Fuel Consumption"]
        response.append(header)
        for car in self.data.Cars.values():
            response.append([car.make, car.model, car.year, car.vin, car.color, car.mileage, car.fuel_consumption])
        return response

# Create object instance
Cars_db = create_cars_db()
# Call both methods for testing
# Cars_db.list_cars()
print(Cars_db.serialize_cars())