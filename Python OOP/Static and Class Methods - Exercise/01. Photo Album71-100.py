from math import ceil

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]
        
    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))
    
    def add_photo(self, label):
        if len(self.photos[-1]) == 4:
            return "No more free slots"
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {self.photos[i].index(label) + 1}."
            
    def display(self):
        result = "\n-----------\n"
        for i in range(self.pages):
            for j in range(len(self.photos[i])):
                result += "[] "
            if len(self.photos[i]) != 0:
                result = result.strip()
            result += "\n-----------\n"
        return result
