email = input()


    
class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError
    email = input()
