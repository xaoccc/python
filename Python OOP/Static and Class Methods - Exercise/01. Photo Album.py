from math import ceil

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]

        
    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))
    
    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i} slot {i}".
            
    def display(self):
        result = "-----------"
        return "-----------"
        

album = PhotoAlbum.from_photos_count(8)
print(album.pages)
