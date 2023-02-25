class Dispo:
    total_km = 0

    def __init__(self):
        self.truck = input("Enter plate number: ")
        self.driver = input("Enter driver name: ")
        self.total_km = 0
        self.avg_km = 0
        self.days = 0
        self.km = -1

    def get_km(self):
        while self.km != 0:
            self.km = int(input("Enter km:"))
            self.total_km += self.km
            self.days += 1

    def show_km(self):
        return self.total_km

    def avg_km_(self):
        return self.total_km / self.days


all_drivers = []

drivers_num = int(input("Number of trucks:"))
for i in range(drivers_num):
    truck_data = []
    dispo = Dispo()
    dispo.get_km()
    truck_data.append(dispo.driver)
    truck_data.append(dispo.truck)
    truck_data.append(dispo.show_km())
    truck_data.append(dispo.avg_km_())
    all_drivers.append(truck_data)
print(all_drivers)