from project.user import User
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan
from project.route import Route


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []
        
    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
    
    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
        if vehicle_type not in vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(vehicle_types[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
            
    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                route.is_locked = True
                
        route_id = len(self.routes) + 1
        self.routes.append(Route(start_point, end_point, length, route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."
    
    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        current_user, current_vehicle, current_route = self.users[0], self.vehicles[0], self.routes[0]
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                current_user = user
                if user.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                current_vehicle = vehicle
                if vehicle.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        for route in self.routes:
            if route.route_id == route_id:
                current_route = route
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                
        if is_accident_happened:
            current_vehicle.change_status()
            current_user.decrease_rating()
        
        else:
            current_user.increase_rating()
            
        current_vehicle.drive(current_route.length)
        return current_vehicle

    def repair_vehicles(self, count: int):

        damaged_vehicles = sorted([v for v in self.vehicles if v.is_damaged], key=lambda x: (x.brand, x.model))
        first_count_vehicles = damaged_vehicles[:count]

        for v in first_count_vehicles:
            v.change_status()
            v.battery_level = 100

        return f"{len(first_count_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***"
        sorted_users = list(sorted(self.users, key=lambda user: -user.rating))
        for user in sorted_users:
            result += f"\n{user}"
        return result



