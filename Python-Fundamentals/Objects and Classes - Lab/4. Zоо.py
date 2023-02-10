# We read all data we have - 
class Zoo:
    #The Zoo class has 1 ATTRIBUTE - __animals
    __animals = 0
    # The __init__ method has 1 PARAMETER - name
    def __init__(self, name):
        self.name = name 
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
            
        Zoo.__animals += 1
#Here we take the input from species_info and we use is as species      
    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Mammals in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Mammals in {self.name}: {', '.join(self.birds)}\n"
            
        result += f"Total animals: {Zoo.__animals}"
        return result

# We get the zoo name
zoo_name = input()
# Add the zoo name as an INSTANCE VARIABLE, i.e. a local vabiable, which we now can access inside the class by typing self.name
zoo = Zoo(zoo_name)
# We get the number of animals in the zoo
total_animals = int(input())
for i in range(total_animals):
    animal = input().split()
    zoo.add_animal(animal[0], animal[1])

species_info = input()
print(zoo.get_info(species_info))
