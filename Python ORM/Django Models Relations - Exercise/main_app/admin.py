from django.contrib import admin

# Register your models here.
from .models import Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "year", "owner", "car_details"]

    @staticmethod
    def car_details(obj: object):
        try:
            owner_name = obj.owner.name
        except AttributeError:
            owner_name = "No owner"

        try:
            registration_number = obj.registration.registration_number
        except AttributeError:
            registration_number = "No registration number"

        return f"Owner: {owner_name}, Registration: {registration_number}"

    car_details.short_description = "Car Details"
