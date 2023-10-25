from django.db import models

class Pet(models.Model):

    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)

class Artifact(models.Model):
    name = models.CharField(max_length=70)
    origin = models.CharField(max_length=70)
    age = models.PositiveIntegerField()
    description = models.TextField()
    is_magical = models.BooleanField(default=False)

#Not migrated models. Migrate them 1 by 1:
class Location(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    population = models.PositiveIntegerField()
    description = models.TextField()
    is_capital = models.BooleanField(default=False)
