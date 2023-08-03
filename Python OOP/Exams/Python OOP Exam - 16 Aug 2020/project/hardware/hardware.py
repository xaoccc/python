from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware

class Hardware:
    def __init__(self, name,  hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        for s in self.software_components:
            if s.name == software.name:
                self.software_components.remove(s)


