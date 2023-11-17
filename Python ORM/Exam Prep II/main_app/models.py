from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from main_app.model_mixins import CreatedMixin


# Create your models here.
class Profile(CreatedMixin):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)


class Product(CreatedMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.1)])
    in_stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)


class Order(CreatedMixin):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_order")
    products = models.ManyToManyField(Product, related_name="products_order")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.1)])
    is_completed = models.BooleanField(default=False)

