from django.contrib import admin

from .models import Book, Exercise


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
