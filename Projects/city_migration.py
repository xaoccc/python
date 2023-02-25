class City:
    def __init__(self, name, population, religion, gender, age):
        self.name = name
        self.population = population
        self.religion = religion
        self.gender = gender
        self.age = age
        self.database = []

    def immigrate(self):
        if person.religion in self.religion.keys():
            self.religion[person.religion] += 1
        if person.gender in self.gender.keys():
            self.gender[person.gender] += 1
        if person.age <= 18:
            self.age["0-18"] += 1
        elif 18 < person.age <= 70:
            self.age["19-70"] += 1
        elif person.age > 70:
            self.age["70+"] += 1
    
    def emigrate(self):
        if person.religion in self.religion.keys():
            self.religion[person.religion] -= 1
        if person.gender in self.gender.keys():
            self.gender[person.gender] -= 1
        if person.age <= 18:
            self.age["0-18"] -= 1
        elif 18 < person.age <= 70:
            self.age["19-70"] -= 1
        elif person.age > 70:
            self.age["70+"] -= 1
    
class Person:
    def __init__(self, religion, gender, age, migrate):
        self.religion = religion
        self.gender = gender
        self.age = age
        self.migrate = migrate
 
name =  input()  
religion = {"christian": 8200, "muslim": 5400, "other": 248}
population = religion["christian"] + religion["muslim"] + religion["other"]
gender = {"male": 6232, "women": 7616}
age = {"0-18": 2770, "19-70": 8215, "70+": 2863}

person = Person(input(), input(), int(input()), input())
city = City(name, population, religion, gender, age)   

print(f"{city.name}\n{city.religion}\n{city.gender}\n{city.age}")

if person.migrate == "immigrant":
    city.immigrate()
elif person.migrate == "emigrant":
    city.emigrate()
    
print(f"{city.name}\n{city.religion}\n{city.gender}\n{city.age}")
