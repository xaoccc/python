
import re
email = input()

pattern = r'[\w\W]+@'
domains = ["com", "org", "bg", "net"]
    
class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass

class NameTooShort(Exception):
    """Name must be more than 4 characters"""
    pass

class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass

while email != "End":
    name_check = re.findall(pattern, email)
    domain_check = email.split(".")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(name_check[0][:-1]) < 5:
        raise NameTooShort("Name must be more than 4 characters")
    elif domain_check[-1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
    email = input()
