from _pydecimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q, Count, Sum
from django.db.models.aggregates import Count, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type):
        return RealEstateListing.objects.filter(property_type=property_type)

    def in_price_range(self, min_price, max_price):
        return RealEstateListing.objects.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

    def with_bedrooms(self, bedrooms_count):
        return RealEstateListing.objects.filter(bedrooms=bedrooms_count)


    def popular_locations(self):
        return (
            RealEstateListing.objects
            .values("location")
            .annotate(location_count=Count("location"))
            .order_by("location_count", "id")
        )[0:2]



class VideoGameManager(models.Manager):
    def games_by_genre(self, genre):
        return VideoGame.objects.filter(genre=genre)

    def recently_released_games(self, year):
        return VideoGame.objects.filter(release_year__gte=year)


    def highest_rated_game(self):
        return VideoGame.objects.values("title").order_by("-rating")[0]["title"]


    def lowest_rated_game(self):
        return VideoGame.objects.values("title").order_by("rating")[0]["title"]


    def average_rating(self):
        # This should be working!!!
        # return VideoGame.objects.annotate(Avg('rating')).values("rating")
        result = 0
        all_ratings = VideoGame.objects.values_list("rating")
        for rating in all_ratings:
            result += rating[0]

        return round(result / len(all_ratings), 1)



# Create your models here.


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    objects = RealEstateListingManager()

class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990, "The release year must be between 1990 and 2023"),
            MaxValueValidator(2023, "The release year must be between 1990 and 2023")
        ]
    )
    rating = models.DecimalField(max_digits=2,decimal_places=1, validators=[
            MinValueValidator(0.0, "The rating must be between 0.0 and 10.0"),
            MaxValueValidator(10.0, "The rating must be between 0.0 and 10.0")
    ])

    objects = VideoGameManager()

    def __str__(self):
        return self.title


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    @staticmethod
    def get_invoices_with_prefix(prefix):
        return Invoice.objects.filter(invoice_number__startswith=prefix)

    @staticmethod
    def get_invoices_sorted_by_number():
        return Invoice.objects.order_by("invoice_number")

    @staticmethod
    def get_invoice_with_billing_info(invoice_number):
        return Invoice.objects.get(invoice_number=invoice_number)


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    @classmethod
    def get_programmers_with_technologies(cls):
        return Programmer.objects.prefetch_related("projects__technologies_used")


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    @classmethod
    def get_projects_with_technologies(cls):
        return Project.objects.prefetch_related("programmers")


class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
