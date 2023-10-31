import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book

# Import your models here

# Create queries within functions
def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []

    for author in authors:
        author_books = Book.objects.filter(author=author).values_list("title", flat=True)
        if author_books:
            result.append(f"{author.name} has written - {', '.join(author_books)}!")

    return "\n".join(result)

def delete_all_authors_without_books():
    authors = Author.objects.all()
    for author in authors:
        if not Book.objects.filter(author=author).values_list("title", flat=True):
            author.delete()
