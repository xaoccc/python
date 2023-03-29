from django.urls import path
from .views import landing_page, create_phone_number

urlpatterns = [
    path('', landing_page, name="landing-page"),
    path('new-contact', create_phone_number, name="new-contact")
]
