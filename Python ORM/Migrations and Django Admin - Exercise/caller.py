import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Shoe, Person

def add_shoes():

    shoe1 = Shoe(
        brand="Nike",
        size=34
    )
    shoe1.save()

    shoe2 = Shoe(
        brand="Nike",
        size=31
    )
    shoe2.save()

    shoe3 = Shoe(
        brand="Adidas",
        size=45
    )
    shoe3.save()

    shoe4 = Shoe(
        brand="Adidas",
        size=42
    )
    shoe4.save()

    shoe5 = Shoe(
        brand="Puma",
        size=21
    )
    shoe5.save()


    return "5 Shoes added to the database"

def add_person():
    person1 = Person(
        name = "Vanessa",
        age = 4
    )
    person1.save()

    return "Person added to the database"

# Create queries within functions
# print(add_person())