from project.hardware.hardware import Hardware
from math import floor

class HeavyHardware(Hardware):
    def __init__(self, name,  capacity, memory):
        super().__init__(name,  "Heavy", capacity * 2, floor(memory * 0.75))