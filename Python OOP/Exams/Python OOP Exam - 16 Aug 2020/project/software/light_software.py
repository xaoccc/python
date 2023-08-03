from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, software_type="Light"):
        super().__init__(name, capacity_consumption // 2, memory_consumption // 2, software_type)


