class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.get_area = width * height

    def __lt__(self, other):
        return self.get_area < other.get_area

    def __le__(self, other):
        return self.get_area <= other.get_area

    def __eq__(self, other):
        return self.get_area == other.get_area

    def __ne__(self, other):
        return self.get_area != other.get_area

    def __gt__(self, other):
        return self.get_area > other.get_area

    def __ge__(self, other):
        return self.get_area >= other.get_area



