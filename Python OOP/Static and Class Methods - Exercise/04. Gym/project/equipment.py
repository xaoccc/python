class Equipment:
    id = 1
    def __init__(self, name):
        self.name = name
        self.id = Equipment.id
    
    @staticmethod    
    def get_next_id():
        next_id = Equipment.id
        Equipment.id += 1
        return next_id
        
    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"