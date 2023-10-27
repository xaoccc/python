import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ready_to_use_django_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop

# Import your models
# Create and check models
# Run and print your queries


def show_highest_rated_art():
    for art in ArtworkGallery.objects.order_by("-rating").first():
        return art


def bulk_create_arts(first_art, second_art):
    first_art.save()
    second_art.save()


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    for laptop in Laptop.objects.order_by("-price", "-id").first():
        return laptop


def bulk_create_laptops(*args):
    for laptop in args:
        laptop.save()


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    updates = {
        "Asus": "Windows",
        "Apple": "MacOS",
        "Dell": "Linux",
        "Acer": "Linux",
        "Lenovo": "Chrome OS"
    }
    all_laptops = Laptop.objects.all()
    for laptop in all_laptops:
        laptop.update(operation_system=updates[laptop.brand])

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()

