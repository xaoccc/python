import os
import django
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Song, Artist, Product, Review

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



# test code
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")

# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=Author.objects.get(name="J.K. Rowling")
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=Author.objects.get(name="George Orwell")
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=Author.objects.get(name="Harper Lee")
# )

# Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)

# Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())

# 02. Music App
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
    current_artist = Artist.objects.get(name=artist_name)
    return Song.objects.filter(artists=current_artist).order_by("-id")

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

# test code

# Create artists
# artist1 = Artist.objects.get(name="Daniel Di Angelo")
# artist2 = Artist.objects.get(name="Indila")

# Create songs
# song1 = Song.objects.get(title="Lose Face")
# song2 = Song.objects.get(title="Tourner Dans Le Vide")
# song3 = Song.objects.get(title="Loyalty")

# Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")

# Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")

# Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")

# Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")

# Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


# 03. Shop
def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    return Review.objects.filter(product=product).aggregate(Avg("rating"))["rating__avg"]

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gt=threshold)

def get_products_with_no_reviews():
    reviews_products_id = Review.objects.values_list("product", flat=True)
    products = Product.objects.exclude(id__in=reviews_products_id).order_by("-name")
    return products

def delete_products_without_reviews():
    reviews_products_id = Review.objects.values_list("product", flat=True)
    for product in Product.objects.exclude(id__in=reviews_products_id).order_by("-name"):
        product.delete()

# Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")

# Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)

# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
#
# print(calculate_average_rating_for_product_by_name("Laptop"))
#
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")
# print(get_reviews_with_high_ratings(1))


def calculate_licenses_expiration_dates():
    pass


def get_drivers_with_expired_licenses(due_date):
    pass


def register_car_by_owner(owner: object):
    pass
