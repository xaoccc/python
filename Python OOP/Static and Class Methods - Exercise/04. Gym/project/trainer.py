class Trainer:
    id = 1
    def __init__(self, name):
        self.name = name
        self.id = Trainer.id
        
    @staticmethod
    def get_next_id():
        next_id = Trainer.id
        Trainer.id += 1
        return next_id
    
    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"