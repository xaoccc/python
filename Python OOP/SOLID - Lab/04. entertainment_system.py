from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, device1, device2):
        pass


class HDMI(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via HDMI"


class RCACable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via RCA"


class EthernetCable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via Ethernet"


class PowerOut(Cable):
    def connect(self, destination, _):
        return f"Connect to power"



class Television():
    pass


class DVDPlayer():
    pass


class GameConsole():
    pass



