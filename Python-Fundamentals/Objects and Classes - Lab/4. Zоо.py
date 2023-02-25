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
    # 7. ... and we come here and add the animal data for each iteration of the loop on line 40:
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        #8. For each added animal, we increase the total number of animals by one    
        Zoo.__animals += 1
    # 10. Here we take the input from species_info and we use is as a filter (species parameter)      
    def get_info(self, species):
        # 11. We have a 3-step result output:
        # 11.1 We define a variable
        result = ""
        # 11.2 Add filtered data in the variable
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
<<<<<<< Updated upstream
        # 11.3 Then add common data in the variable result    
=======
            
>>>>>>> Stashed changes
        result += f"Total animals: {Zoo.__animals}"
        # 12. Return the result
        return result

# 1. We get the zoo name
zoo_name = input()
# 2. Add the zoo name as an INSTANCE VARIABLE, i.e. a local vabiable, which we now can access inside the class by typing self.name
zoo = Zoo(zoo_name)
# 3. We get the number of animals in the zoo
total_animals = int(input())
for i in range(total_animals):
    # 4. We receive each animal species and name
    animal = input().split()
    # 5. We get the two parameters of the add_animal() method 
    species = animal[0]
    name = animal[1]
    # 6. Add the parameters for each iteration...
    zoo.add_animal(species, name)
# 9. After the loop and the add_animal() method have finished their work, we get here and write a species name to filter
species_info = input()
# 13. Print the result from get_info() method from zoo class instance / zoo object. Remember - class Zoo is an empty template, object zoo is already filled with data
print(zoo.get_info(species_info))
