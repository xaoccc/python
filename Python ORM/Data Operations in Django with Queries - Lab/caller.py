import os
import django
from main_app.models import Student
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def add_students():
    student1 = Student(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date="15/05/1995",
        email="john.doe@university.com"
    )
    student1.save()

    student2 = Student(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        birth_date="null",
        email="jane.smith@university.com"
    )
    student2.save()

    student3 = Student(
        student_id="FH2014",
        first_name="Alice",
        last_name="Johnson",
        birth_date="10/02/1998",
        email="alice.johnson@university.com"
    )
    student3.save()

    student4 = Student(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date="25/11/1996",
        email="bob.wilson@university.com"
    )
    student4.save()

# Import your models
# Create and check models
# Run and print your queries


add_students()
# print(Student.objects.all())
