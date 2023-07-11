from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name, capacity=30):
        super().__init__(name, capacity)
        
    def details(self):
        return f"{self.name} Main Service:\nRobots: {' '.join([robot.name for robot in self.robots]) if self.robots else 'none'}" 
