from project.computer_types.computer import Computer

class Laptop(Computer):

    def configure_computer(self, processor, ram):
        processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }
        if processor not in processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
            
        valid_ram = [2, 4, 8, 16, 32, 64]
        if ram > 64 or ram not in valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
            
        for r in range(len(valid_ram)):
            if 2 ** (r + 1) == ram:
                self.price = 100 * (r + 1)
                break
        self.ram = ram
        self.processor = processor
        self.price += processors[processor]
        return  f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for { self.price}$."