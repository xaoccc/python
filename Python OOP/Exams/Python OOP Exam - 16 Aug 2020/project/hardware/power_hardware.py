from math import floor
from project.hardware.hardware import Hardware

class PowerHardware(Hardware):
    def __init__(self, name,  capacity, memory, hardware_type):
        super().__init__(name,  "Power", floor(capacity * 0.25), floor(memory * 1.75), hardware_type)