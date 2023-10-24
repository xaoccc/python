import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact

# Create queries within functions

def create_pet(name, species):
    pet = Pet(
        name=name,
        species=species
    )
    pet.save()
    return f"{name} is a very cute {species}!"


# test_code
# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact (
        name = name,
        origin = origin,
        age = age,
        description = description,
        is_magical = is_magical
    )
    artifact.save()
    return f"The artifact {name} is {age} years old!"

def delete_all_artifacts():
    Artifact.objects.all().delete()

# test code
# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))
# delete_all_artifacts()