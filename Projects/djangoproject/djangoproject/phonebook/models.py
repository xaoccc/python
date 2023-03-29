from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(unique=True)
