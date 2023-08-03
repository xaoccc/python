from math import floor

from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, software_type="Light"):
        super().__init__(name, floor(capacity_consumption / 2), floor(memory_consumption / 2), software_type)


