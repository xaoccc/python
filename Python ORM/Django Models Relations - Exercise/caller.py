import os
import django
from django.core.exceptions import ObjectDoesNotExist

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song

# Import your models here

# Create queries within functions
def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []

    for author in authors:
        author_books = Book.objects.filter(author=author).values_list("title", flat=True)
        if author_books:
            result.append(f"{author.name} has written - {', '.join(author_books)}!")

    return "\n".join(result)

def delete_all_authors_without_books():
    authors = Author.objects.all()
    for author in authors:
        if not Book.objects.filter(author=author).values_list("title", flat=True):
            author.delete()


def add_song_to_artist(artist_name: str, song_title: str):
    # Because get() raises and exception if number of returned objects are not exactly 1, we might want to catch it:
    try:
        artist = Artist.objects.get(name=artist_name)
    except ObjectDoesNotExist:
        print(f"Artist '{artist_name}' does not exist.")
        return

    try:
        song, created = Song.objects.get_or_create(title=song_title)
        artist.songs.add(song)
    except Exception as e:
        print(f"An error occurred: {e}")

def get_songs_by_artist(artist_name: str):
    return Artist.objects.filter(name=artist_name).value("songs")

def remove_song_from_artist(artist_name: str, song_title: str):
    try:
        artist = Artist.objects.get(name=artist_name)
    except ObjectDoesNotExist:
        print(f"Artist '{artist_name}' does not exist.")

    try:
        song = Song.objects.get(title=song_title)
    except ObjectDoesNotExist:
        print(f"Song '{song_title}' does not exist.")

    try:
        artist.songs.remove(song)
    except Exception as e:
        print(f"An error occurred: {e}")


