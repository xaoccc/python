from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def find_hardware(hardware_name, available_hardware):
        for hardware in available_hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def find_software(software_name, available_software):
        for software in available_software:
            if software.name == software_name:
                return software

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))


    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))


    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware =  System.find_hardware(hardware_name, System._hardware)
        if not current_hardware:
            return "Hardware does not exist"

        current_hardware.install(ExpressSoftware(name, capacity_consumption, memory_consumption))
        System._software.append(ExpressSoftware(name, capacity_consumption, memory_consumption))

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware = System.find_hardware(hardware_name, System._hardware)
        if not current_hardware:
            return "Hardware does not exist"

        current_hardware.install(LightSoftware(name, capacity_consumption, memory_consumption))
        System._software.append(LightSoftware(name, capacity_consumption, memory_consumption))


    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        current_hardware = System.find_hardware(hardware_name, System._hardware)
        current_software = System.find_software(software_name, System._software)

        if not current_hardware or not current_software:
            return "Some of the components do not exist"

        System._software.remove(current_software)
        current_hardware.uninstall(current_software)



    @staticmethod
    def analyze():
        return f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\nTotal Operational Memory: {sum([soft.memory_consumption for soft in System._software])} / {sum([hard.memory for hard in System._hardware])}\nTotal Capacity Taken: {sum([soft.capacity_consumption for soft in System._software])} / {sum([hard.capacity for hard in System._hardware])}"



    @staticmethod
    def system_split():
        result = []
        for hard_component in System._hardware:
            result.append(f"Hardware Component - {hard_component.name}")
            result.append(f"Express Software Components: {sum([1 for component in hard_component.software_components if component.software_type == 'Express'])}")
            result.append(f"Light Software Components: {sum([1 for component in hard_component.software_components if component.software_type == 'Light'])}")
            result.append(f"Memory Usage: {sum([component.memory_consumption for component in hard_component.software_components])} / {hard_component.memory}")
            result.append(f"Capacity Usage: {sum([component.capacity_consumption for component in hard_component.software_components])} / {hard_component.capacity }")
            result.append(f"Type: {hard_component.hardware_type}")
            if len([component for component in hard_component.software_components]) == 0:
                result.append(f"Software Components: None")
            else:
                result.append(f"Software Components: {', '.join([soft_component.name for soft_component in hard_component.software_components])}")

        return str("\n".join(result))

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())

