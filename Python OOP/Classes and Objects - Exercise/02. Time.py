class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    
    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    
    def get_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"
        
    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
                    
            self.seconds = 0
        return self.get_time()
