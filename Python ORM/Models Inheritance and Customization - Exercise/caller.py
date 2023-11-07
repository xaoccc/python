import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student



# Retrieving student IDs from the database
retrieved_student1 = Student.objects.get(name="John")
retrieved_student2 = Student.objects.get(name="Alice")
retrieved_student3 = Student.objects.get(name="Bob")

print(retrieved_student1.student_id)
print(retrieved_student2.student_id)
print(retrieved_student3.student_id)

