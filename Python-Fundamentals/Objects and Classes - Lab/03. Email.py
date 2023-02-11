class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
        
    def send(self):
        self.is_sent = True
        
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

command = input()
all_mail = []

while command != "Stop":
    command = command.split()
    email = Email(command[0], command[1], command[2])
    all_mail.append(email)
    command = input()
sent_info = [int(i) for i in input().split(", ")]

for i in sent_info:
    all_mail[i].send()
    
for email in all_mail:
    print(email.get_info())
