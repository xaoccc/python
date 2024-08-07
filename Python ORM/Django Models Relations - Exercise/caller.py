import os
from datetime import timedelta

import django
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Sum, Count
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Song, Artist, Product, Review, DrivingLicense, Driver, Owner, Car, Registration


# Import your models here

# Create queries within functions
def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by("id")
    result = []

    for author in authors:
        author_books = Book.objects.filter(author=author).values_list("title", flat=True)
        if author_books:
            result.append(f"{author.name} has written - {', '.join(author_books)}!")

    return "\n".join(result)

def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()



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
        song = Song.objects.get(title=song_title)
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
    reviews = product.reviews.all()

    total_rating = sum(r.rating for r in reviews)
    average_rating = total_rating / len(reviews)
    return average_rating

    # Optimized solution:
    # Product.objects.annotate(
    #     total_ratings=Sum("review__rating"),
    #     num_reviews=Count("review")
    # ).get(name=product_name)
    # return product.total_ratings / product.num_reviews

    # My solution:
    # try:
    #     product = Product.objects.get(name=product_name)
    #     return Review.objects.filter(product=product).aggregate(Avg("rating"))["rating__avg"]
    # except Product.objects.model.DoesNotExist:
    #     return "Product does not exist!"

def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)

def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")

def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


# print(get_products_with_no_reviews())
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")

# print(calculate_average_rating_for_product_by_name("Laptop"))

# before_deletion = Product.objects.count()
# print(f"Products before deletion: {before_deletion}")
# delete_products_without_reviews()
# print(f"Products deleted: {before_deletion - Product.objects.count()}")
# print(f"Products left: {Product.objects.count()}")

# high_rating_reviews = get_reviews_with_high_ratings(3)
# for review in high_rating_reviews:
#     print(f"Rating: {review.rating}, Description: {review.description}")

# print(get_reviews_with_high_ratings(3))

# 04. License
def calculate_licenses_expiration_dates():
    all_licenses = DrivingLicense.objects.all().order_by("-license_number")
    result = []
    for dr_license in all_licenses:
        result.append(f"License with id: {dr_license.license_number} expires on {dr_license.issue_date + timedelta(days=365)}!")
    return "\n".join(result)

def get_drivers_with_expired_licenses(due_date):
    all_licenses = DrivingLicense.objects.filter(issue_date__gte=due_date - timedelta(days=364))
    result = []
    for driver in all_licenses:
        result.append(driver.driver)
    return result

# test code

# print(calculate_licenses_expiration_dates())
#
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2024, 4, 24))
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")

def register_car_by_owner(owner: object):

    first_free_car = Car.objects.filter(registration__isnull=True, owner=owner).first()
    first_free_car.owner = owner
    first_free_car.save()

    first_available_reg = Registration.objects.filter(car__isnull=True).first()
    first_available_reg.registration_date, first_available_reg.car = date.today(), first_free_car
    first_available_reg.save()

    return f"Successfully registered {first_free_car.model} to {owner.name} with registration number {first_available_reg.registration_number}."

# test code:

# owner1 = Owner.objects.get(name='Ivelin Milchev')
# owner2 = Owner.objects.get(name='Alice Smith')
#
# car1 = Car.objects.get(model='Citroen C5', year=2004)
# car2 = Car.objects.get(model='Honda Civic', year=2021)
#
# registration1 = Registration.objects.get(registration_number='TX0044XA')
# registration2 = Registration.objects.get(registration_number='XYZ789')
#
# print(register_car_by_owner(owner2))


