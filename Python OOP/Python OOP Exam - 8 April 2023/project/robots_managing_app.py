from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []
        
    def add_service(self, service_type: str, name: str):
        valid_services = {"MainService": MainService, "SecondaryService": SecondaryService}
        if service_type not in valid_services:
            raise Exception("Invalid service type!")
        self.services.append(valid_services[service_type](name))
        return f"{service_type} is successfully added."
        
    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robots = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}
        if robot_type not in valid_robots:
            raise Exception("Invalid robot type!")
        self.robots.append(valid_robots[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."
        
    def add_robot_to_service(self, robot_name: str, service_name: str):
        for robot in self.robots:
            if robot.name == robot_name:
                current_robot = robot
                break
        
        for service in self.services:
            if service.name == service_name:
                current_service = service
                break
        r_type, s_type = current_robot.__class__.__name__, current_service.__class__.__name__
        if ( r_type == "MaleRobot" and s_type == "SecondaryService") or (r_type == "FemaleRobot" and s_type == "MainService"):
            return "Unsuitable service."
            
        if current_service.capacity == len(current_service.robots):
            raise Exception("Not enough capacity for this robot!") 
            
        self.robots.remove(current_robot)
        current_service.robots.append(current_robot)
        return f"Successfully added {robot_name} to {service_name}."
        
    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_robot = ""

        for service in self.services:
            if service.name == service_name:
                current_service = service
                for robot in current_service.robots:
                    if robot.name == robot_name:
                        current_robot = robot
        
        if not current_robot:
            raise Exception("No such robot in this service!")
        
        current_service.robots.remove(current_robot)
        self.robots.append(current_robot)
        return f"Successfully removed {robot_name} from {service_name}."
        
    def feed_all_robots_from_service(self, service_name: str):
        for service in self.services:
            if service.name == service_name:
                current_service = service
                break
            
        for robot in current_service.robots:
            robot.eating()
            
        return f"Robots fed: {len(current_service.robots)}."
        
    def service_price(self, service_name: str):
        total_price = 0
        for service in self.services:
            if service.name == service_name:
                current_service = service
                break
        
        for robot in current_service.robots:
            total_price += robot.price
        
        return f"The value of service {service_name} is {total_price:.2f}."
        
    def __str__(self):
        result = ""
        for service in self.services:
            result += f"{service.details()}\n"
        return result.strip()