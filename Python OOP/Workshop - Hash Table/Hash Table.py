class HashTable:
    def __init__(self):
        self.__size = 4
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size
        self.__length = 0


    def find_index(self, test):
        current_index = sum([ord(char) for char in test]) % self.__size

        while True:
            if not self.__keys[current_index % self.__size]:
                return current_index % self.__size
            current_index += 1

    def add(self, key, value):
        self[key] = value


    def __len__(self):
        return self.__length

    def __setitem__(self, key, value):
        if len(self) == self.__size:
            self.__resize()

        index = self.find_index(key)
        self.__keys[index] = key
        self.__values[index] = value
        self.__length += 1

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("No such key in hash table!")

    def get(self, key):
        return self.__getitem__(key)

    def __resize(self):
        self.__keys +=  [None] * self.__size
        self.__values +=  [None] * self.__size
        self.__size *= 2

    def __repr__(self):
        result = []
        for i in range(len(self.__keys)):
            if self.__keys[i]:
                result.append(f"{self.__keys[i]}: {self.__values[i]}")
        return "{" + ', '.join(result) + "}"





table = HashTable()
table["name"] = "Pesho"


table["age"] = 40
table["has_dog"] = True
table["has_cat"] = False
print(table._HashTable__keys)
print(table._HashTable__values)
table["has_bear"] = False
table.add("car","Golf")

print(table)
print(table.get("age"))
print(table["name"])

