from project.hardware.hardware import Hardware
from math import floor

class HeavyHardware(Hardware):
    def __init__(self, name,  capacity, memory, hardware_type="Heavy"):
        super().__init__(name,  capacity * 2, floor(memory * 0.75), hardware_type)