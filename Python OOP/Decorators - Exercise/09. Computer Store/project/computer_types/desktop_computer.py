from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    def configure_computer(self, processor, ram):
        processors = {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }
        if processor not in processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
            
        valid_ram = [2, 4, 8, 16, 32, 64, 128]
        if ram not in valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
            
        for r in range(len(valid_ram)):
            if 2 ** (r + 1) == ram:
                self.price = 100 * (r + 1)
                break
        self.ram = ram
        self.processor = processor
        self.price += processors[processor]
        return  f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for { self.price}$."
