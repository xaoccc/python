from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from main_app.validators import validate_name, validate_phone

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, "Age must be greater than 18")])
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, validators=[validate_phone])
    website_url = models.URLField()

class BaseMedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
        ordering=["-created_at", "title"]

class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, "Author must be at least 5 characters long")]
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, "ISBN must be at least 6 characters long")]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, "Director must be at least 8 characters long")]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, "Artist must be at least 9 characters long")]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        pass

    def calculate_shipping_cost(self, weight):
        pass

    def format_product_name(self):
        return f"Product: {self.name}"

class DiscountedProduct(Product):

    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        pass

    def calculate_tax(self):
        pass

    def calculate_shipping_cost(self, weight):
        pass


    def format_product_name(self):
        return f"Discounted Product: {self.name}"



