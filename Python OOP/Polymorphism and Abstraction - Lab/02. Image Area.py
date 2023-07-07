class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height        

    def get_area(self):
        return self.width * self.height
    
    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    def __eq__(self, other):
        return self.area == other.area




