from project.booths.booth import Booth

class OpenBooth(Booth):

    def reserve(self, number_of_people: int):
        self.price_for_reservation = 2.50 * number_of_people
        self.is_reserved = True