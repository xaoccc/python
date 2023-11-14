from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q, F
from main_app.managers import RealEstateListingManager, VideoGameManager

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

    @staticmethod
    def overdue_high_priority_tasks():
        return Task.objects.filter(Q(priority="High") & Q(is_completed=False) & Q(completion_date__gt=F("creation_date")))

    @staticmethod
    def completed_mid_priority_tasks():
        return Task.objects.filter(Q(priority="Medium") & Q(is_completed=True))

    @staticmethod
    def search_tasks(query):
        return Task.objects.filter(Q(title__contains=query) | Q(description__contains=query))

    @staticmethod
    def recent_completed_tasks(days):
        return Task.objects.filter(Q(is_completed=True) & Q(completion_date__gte=F("creation_date") - days))


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    @staticmethod
    def get_long_and_hard_exercises():
        return Exercise.objects.filter(Q(duration_minutes__gt=30) & Q(difficulty_level__gte=10))

    @staticmethod
    def get_short_and_easy_exercises():
        return Exercise.objects.filter(Q(duration_minutes__lt=15) & Q(difficulty_level__lt=5))

    @staticmethod
    def get_exercises_within_duration(min_duration: int, max_duration: int):
        return Exercise.objects.filter(Q(duration_minutes__gte=min_duration) & Q(duration_minutes__lte=max_duration))

    @staticmethod
    def get_exercises_with_difficulty_and_repetitions(min_difficulty: int, min_repetitions: int):
        return Exercise.objects.filter(Q(difficulty_level__gte=min_difficulty) & Q(repetitions__gte=min_repetitions))
