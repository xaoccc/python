from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
    
    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
            
    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
            
    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
            
    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)
    
    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
            
    def subscription_info(subscription_id): 
        return "\n".join(
            str(x) for info in (self.subscriptions, self.customers, self.trainers, self.equipment, self.plans)
            for x in info if x.id == subscription_id)