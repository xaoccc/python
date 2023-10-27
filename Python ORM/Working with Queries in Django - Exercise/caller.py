import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop

# Import your models
# Create and check models
# Run and print your queries


def show_highest_rated_art():
    best_art = ArtworkGallery.objects.all().order_by("-rating", "id").first()
    return f"{best_art.art_name} is the highest-rated art with a {best_art.rating} rating!"


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    top_laptop = Laptop.objects.order_by("-price", "-id").first()
    return f"{top_laptop.brand} is the most expensive laptop available for {top_laptop.price}$!"



def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
    Laptop.objects.filter(brand="Apple").update(operation_system="MacOS")
    Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
    Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


