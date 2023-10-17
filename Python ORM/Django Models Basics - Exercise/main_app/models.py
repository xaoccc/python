from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()


class Blog(models.Model):
    post = models.TextField()
    author = models.CharField(max_length=35)


class WeatherForecast(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    cook_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)



