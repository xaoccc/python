from abc import ABC, abstractmethod


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyML(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):
    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    def send(self):
        pass


class PostPigeon(ISender):
    def send(self):
        return ''.join(["I'm ", self.sender])


class IRecipient(ABC):
    def __init__(self, recipient):
        self.recipient = recipient

    def receive(self):
        pass


class Bulsatcom(IRecipient):
    def receive(self):
        return ''.join(["I'm ", self.recipient])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.send()

    def set_receiver(self, receiver):
        self.__receiver = receiver.receive()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


my_content = MyML("Hello Python")
this_sender = PostPigeon("A Flying Shitting Fortress")
that_recipient = Bulsatcom("baba Pena ot vtoria etaj")
my_web_page = HTML("Az sam ebasi hakera")
email = Email('IM')
email.set_sender(this_sender)
email.set_receiver(that_recipient)
email.set_content(my_content)
print(email)
email.set_content(my_web_page)
print(email)

