class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    
    def __is_name_valid(self, name):
        return len(name) >= self.min_length
    
    def __is_mail_valid(self, mail):
        return mail in self.mails
        
    def __is_domain_valid(self, domain):
        return domain in self.domains
        
    def validate(self, email):
        name = email.split("@")[0]
        domain = email.split(".")[-1]
        mail = email.split("@")[-1].split(".")[0]
        return self.__is_name_valid(name) and self.__is_domain_valid(domain) and self.__is_mail_valid(mail)
