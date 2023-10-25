import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


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

# Populate table (comment code after first execution):
city1 = Location(name="Sofia", region="Sofia Region", population=1329000,
                 description="The capital of Bulgaria and the largest city in the country", is_capital=False)
city1.save()

city2 = Location(name="Plovdiv", region="Plovdiv Region", population=346942,
                 description="The second-largest city in Bulgaria with a rich historical heritage", is_capital=False)
city2.save()

city3 = Location(name="Varna", region="Varna Region", population=330486,
                 description="A city known for its sea breeze and beautiful beaches on the Black Sea", is_capital=False)
city3.save()


def show_all_locations():
    locations = Location.objects.all().order_by("id")
    result = ""
    for loc in locations:
        result += f"{loc.name} has a population of {loc.population}!\n"
    return result


# Test code:
# print(show_all_locations())


def new_capital():
    locations = Location.objects.all()
    locations.first().capital = True
    locations.first().save()


# Test code:
# print(new_capital())


def get_capitals():
    return Location.objects.filter(is_capital=True).values_list('name', flat=True)


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
        all_cars.price_with_discount = all_cars.price - discount
        car.save()


# Test code:
# apply_discount()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


# Test code:
# print(get_recent_cars())


def delete_last_car():
    Car.objects.last().delete()


# 5. Task
def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)
    result = ""
    for task in unfinished_tasks:
        result += f"Task - {task.title} needs to be done until {task.due_date}!\n"
    return result


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    decoded_new_task = ""
    for char in text:
        decoded_new_task += chr(ord(char)-3)

    for task in Task.objects.filter(title=task_title):
        task.description = decoded_new_task
        task.save()


# test code:
# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title ='Simple Task').description)

# 6. Hotel Room
def get_deluxe_rooms():
    even_id_rooms = HotelRoom.objects.filter(id__mod=2)
    result = ""
    for room in even_id_rooms:
        result += f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!\n"

    return result

def increase_room_capacity():
    rooms = HotelRoom.objects.values('id', 'capacity', 'is_reserved')
    for room in rooms:
        if room.id == HotelRoom.objects.first().id and room.is_reserved:
            room.capacity += room.id

        previous_capacity = room.capacity

        if room.id != HotelRoom.objects.first().id and room.is_reserved:
            room.capacity += previous_capacity

        room.save()


def reserve_first_room():
    HotelRoom.objects.first().is_reserved = True

def delete_last_room():
    HotelRoom.objects.last().delete()

# test code:
# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)

