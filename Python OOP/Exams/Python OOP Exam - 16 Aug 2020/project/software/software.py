class Software:
    name: str
    capacity_consumption: str
    memory_consumption: int
    software_type: int
    def __init__(self, name, software_type, capacity_consumption, memory_consumption):
        self.name = name
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption
        self.software_type = software_type