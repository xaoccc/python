import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Restaurant, Menu




