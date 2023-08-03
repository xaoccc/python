from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption, software_type="Express"):
        super().__init__(name, capacity_consumption, memory_consumption * 2, software_type)