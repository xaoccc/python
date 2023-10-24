import os
import django

from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Student

def add_students():
    student1 = Student(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date="1995-05-15",
        email="john.doe@university.com"
    )
    student1.save()

    student2 = Student(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        birth_date=None,
        email="jane.smith@university.com"
    )
    student2.save()

    student3 = Student(
        student_id="FH2014",
        first_name="Alice",
        last_name="Johnson",
        birth_date="1998-02-10",
        email="alice.johnson@university.com"
    )
    student3.save()

    student4 = Student(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date="1996-11-25",
        email="bob.wilson@university.com"
    )
    student4.save()

# Import your models
# Create and check models
# Run and print your queries

def get_students_info():
    result = ""
    for student in Student.objects.all():
        result += f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}\n"

    return result

def update_students_emails():
    for student in Student.objects.all():
        student.email = student.email.replace("university.com", "uni-students.com")
        student.save()


def truncate_students():
    for student in Student.objects.all():
        student.delete()

# add_students()
# print(get_students_info())

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)
truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")
