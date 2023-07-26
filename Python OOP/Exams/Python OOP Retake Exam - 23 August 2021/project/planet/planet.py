class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strop() == "":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value
