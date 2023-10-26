import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


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
    artifact = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    artifact.save()
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# test code
# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))
# delete_all_artifacts()

# Migrate before test:
# 3. Location


def show_all_locations():
    locations = Location.objects.all().order_by("-id")
    result = []
    for loc in locations:
        result.append(f"{loc.name} has a population of {loc.population}!")
    return "\n".join(result)


# Test code:
# print(show_all_locations())


def new_capital():
    first_location = Location.objects.all().first()
    first_location.is_capital = True
    first_location.save()


# Test code:
# print(new_capital())


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


# Test code:
# print(get_capitals())


def delete_first_location():
    Location.objects.first().delete()


# Test code:
# delete_first_location()
# print(show_all_locations())


# 4. Car
def apply_discount():
    all_cars = Car.objects.all()
    for car in all_cars:
        discount = sum(int(digit) for digit in str(car.year))
        car.price_with_discount = car.price * (100 - discount) / 100
        car.save()


# Test code:
# apply_discount()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


# Test code:
# print(get_recent_cars())


def delete_last_car():
    Car.objects.last().delete()

# delete_last_car()

# 5. Task
def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)
    result = []
    for task in unfinished_tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")
    return "\n".join(result)

# test code:
# print(show_unfinished_tasks())

def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()
# test code:
# complete_odd_tasks()

def encode_and_replace(text: str, task_title: str):
    decoded_new_task = ""
    for char in text:
        decoded_new_task += chr(ord(char) - 3)

    for task in Task.objects.filter(title=task_title):
        task.description = decoded_new_task
        task.save()


# test code:
# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title ='Simple Task').description)

# 6. Hotel Room
def get_deluxe_rooms():

    all_deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    result = []
    for room in all_deluxe_rooms:
        if room.id % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return "\n".join(result)

# test code
# print(get_deluxe_rooms())
def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')
    previous_capacity = 0

    for room in rooms:

        if room.is_reserved:
            if room.id == HotelRoom.objects.first().id:
                room.capacity += room.id
            else:
                room.capacity += previous_capacity
            room.save()

        previous_capacity = room.capacity


# increase_room_capacity()
def reserve_first_room():
    HotelRoom.objects.first().is_reserved = True

def delete_last_room():
    if HotelRoom.objects.last().is_reserved:
        HotelRoom.objects.last().delete()

# test code:

# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)
# delete_last_room()

# 7. Character

def update_characters():
    all_chars = Character.objects.all()

    for char in all_chars:
        if char.class_name == "Mage":
            char.level += 3
            char.intelligence -= 7

        elif char.class_name == "Warrior":
            char.hit_points //= 2
            char.dexterity += 4

        else:
            char.inventory = "The inventory is empty"

def fuse_characters(first_character, second_character):

    char = Character(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=(first_character.level + second_character.level)//2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory="Bow of the Elven Lords, Amulet of Eternal Wisdom" if first_character.class_name in ["Mage", "Scout"] else "Dragon Scale Armor, Excalibur"
    )
    char.save()
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    all_chars = Character.objects.all()
    for char in all_chars:
        char.dexterity = 30
        char.save()


def grand_intelligence():
    all_chars = Character.objects.all()
    for char in all_chars:
        char.intelligence = 40
        char.save()


def grand_strength():
    all_chars = Character.objects.all()
    for char in all_chars:
        char.strength = 50
        char.save()


def delete_characters():
    all_chars = Character.objects.all()
    for char in all_chars:
        if char.inventory == "The inventory is empty":
            char.delete()

