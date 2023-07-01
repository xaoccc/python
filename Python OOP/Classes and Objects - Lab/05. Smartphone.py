class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False
        
    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
    
    def power(self):
        self.is_on = True
    
    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if app_memory <= self.memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        return f"Not enough memory to install {app}"
