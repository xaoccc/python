from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name= name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        
    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        else:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    
    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        else:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    
    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"
    
    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
    
    def tend_animals(self):
        animals_cost = 0
        for animal in self.animals:
            animals_cost += animal.money_for_care
        if self.__budget < animals_cost:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    
    def profit(self, amount):
        self.__budget += amount
    
    def animals_status(self):
        result = ""
        lions, tigers, cheetahs = 0, 0, 0
        animals_data = {"Lion" : [], "Tiger": [], "Cheetah": []}
        
        for animal in self.animals:
            animals_data[animal.__class__.__name__].append(str(animal))
            if animal.__class__.__name__ == "Lion":
                lions += 1
            elif animal.__class__.__name__ == "Tiger":
                tigers += 1
            else:
                cheetahs += 1

        result += f"You have {len(self.animals)} animals"
        result += f"\n----- {lions} Lions:"
        for value in animals_data["Lion"]:
            result += f"\n{value}"
        result += f"\n----- {tigers} Tigers:"
        for value in animals_data["Tiger"]:
            result += f"\n{value}"
        result += f"\n----- {cheetahs} Cheetahs:"
        for value in animals_data["Cheetah"]:
            result += f"\n{value}"
                
        return result

    def workers_status(self):
        result = ""
        keepers, caretakers, vets = 0, 0, 0
        workers_data = {"Keeper" : [], "Caretaker": [], "Vet": []}
        
        for worker in self.workers:
            workers_data[worker.__class__.__name__].append(str(worker))
            if worker.__class__.__name__ == "Keeper":
                keepers += 1
            elif worker.__class__.__name__ == "Caretaker":
                caretakers += 1
            else:
                vets += 1

        result += f"You have {len(self.workers)} workers"
        result += f"\n----- {keepers} Keepers:"
        for value in workers_data["Keeper"]:
            result += f"\n{value}"
        result += f"\n----- {caretakers} Caretakers:"
        for value in workers_data["Caretaker"]:
            result += f"\n{value}"
        result += f"\n----- {vets} Vets:"
        for value in workers_data["Vet"]:
            result += f"\n{value}"
                
        return result