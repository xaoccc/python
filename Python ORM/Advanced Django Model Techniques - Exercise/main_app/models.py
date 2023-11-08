from django.core.validators import MinValueValidator
from django.db import models
from main_app.validators import validate_name, validate_phone

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, "Age must be greater than 18")])
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, validators=[validate_phone])
    website_url = models.URLField()