from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware =  None
        if hardware_name not in [hardware.name for hardware in System._hardware]:
            return "Hardware does not exist"

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                current_hardware = hardware
        current_hardware.install(ExpressSoftware(name, capacity_consumption, memory_consumption))
        System._software.append(ExpressSoftware(name, capacity_consumption, memory_consumption))


    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        pass

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        pass


    @staticmethod
    def analyze():
        pass

    @staticmethod
    def system_split():
        pass

