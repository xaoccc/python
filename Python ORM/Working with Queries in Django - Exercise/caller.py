import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ready_to_use_django_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery

# Import your models
# Create and check models
# Run and print your queries


def show_highest_rated_art():
    for art in ArtworkGallery.objects.order_by("rating").first():
        return art


def bulk_create_arts(first_art, second_art):
    first_art.save()
    second_art.save()


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()