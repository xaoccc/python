import os
from datetime import date

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Technology, Project, Programmer, Task, Exercise

# Import your models
# Create and check models
# Run and print your queries

# Create instances of VideoGame with real data

# Run the custom manager methods

exercises_within_duration = Exercise.get_exercises_within_duration(20, 40)
print(f"Exercises within 20 - 40 minutes:")
for exercise in exercises_within_duration:
    print('- ' + exercise.name)

exercises_with_difficulty_and_repetitions = Exercise.get_exercises_with_difficulty_and_repetitions(6, 15)
print(f"Exercises with difficulty 6+ and repetitions 15+:")
for exercise in exercises_with_difficulty_and_repetitions:
    print('- ' + exercise.name)













