class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.") 
        self.__username = value 
    
    @password.setter
    def password(self, value):
        if len(value) < 8 or value.lower() == value or value.isalpha() or value.isdigit() or not any(char.isdigit() for char in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.") 
        self.__password = value 
        
    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.password)}'
