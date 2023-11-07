import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import CreditCard

credit_card1 = CreditCard.objects.create(card_owner="Krasimir", card_number="1234567890123450")

credit_card1.save()



