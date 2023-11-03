from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    SPECIALIZATIONS = (
        ("Mammals", "Mammals"),
        ("Birds", "Birds"),
        ("Reptiles", "Reptiles"),
        ("Others", "Others")
    )

    specialty = models.CharField(max_length=10, choices=SPECIALIZATIONS)
    managed_animals = models.ManyToManyField(Animal)

    def clean(self):
        # Check if the "specialty" field value is in the list of valid choices
        if self.specialty not in dict(self.SPECIALIZATIONS).keys():
            raise ValidationError("Specialty must be a valid choice.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ZooKeeper, self).save(*args, **kwargs)


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)


class ZooDisplayAnimal(Animal):

    class Meta:
        proxy = True

