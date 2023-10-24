import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet

# Create queries within functions

def create_pet(name, species):
    pet = Pet(
        name=name,
        species=species
    )
    pet.save()
    return f"{name} is a very cute {species}!"



print(create_pet('Buddy', 'Dog'))
print(create_pet('Whiskers', 'Cat'))
print(create_pet('Rocky', 'Hamster'))
