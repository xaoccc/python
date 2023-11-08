from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    categories = ["Appetizers", "Main Course", "Desserts"]

    for category in categories:
        if category.lower() not in value.lower():
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
