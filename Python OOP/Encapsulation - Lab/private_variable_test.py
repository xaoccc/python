class Names:
    def __init__(self, name, egn):
        self.name = name
        self.__egn = egn
    
    def show_private_variable(self):
        return f"But you can access private variables from outside using class methods. The private variable __egn has a value {self.__egn}"

name = Names("Lucifer", 6006066600)  
try:
    print(name.egn)
except AttributeError:
    print("You cannot access private variables directly from outside")

print(name.show_private_variable())
