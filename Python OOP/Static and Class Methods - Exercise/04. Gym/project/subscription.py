class Subscription:
    id = 1
    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.id
        
    @staticmethod
    def get_next_id():
        next_id = Subscription.id
        Subscription.id += 1
        return next_id
        
    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"