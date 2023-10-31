from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=40)


class Book(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=100, unique=True)


class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    songs = models.ManyToManyField(to="Song", related_name="artists")

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Review(models.Model):
    description = models.TextField(max_length=200)
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


