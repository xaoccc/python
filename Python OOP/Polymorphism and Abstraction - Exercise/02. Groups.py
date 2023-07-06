class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __add__(self, other):
        return Person(self.name, other.surname)
        
    def __repr__(self):
        return f"{self.name} {self.surname}"
 
        
class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)
        
    def __len__(self):
        return len(self.people)
        
    def __getitem__(self, idx):
        return f"Person {idx}: {self.people[idx]}"
        
    def __repr__(self):
        people_in_group = []
        for person in self.people:
            people_in_group.append(person.__repr__())
        return f"Group {self.name} with members {', '.join(people_in_group)}"
