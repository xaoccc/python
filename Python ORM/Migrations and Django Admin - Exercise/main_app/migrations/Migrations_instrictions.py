# migrate Item model. Migration 0010_item.py
# create empty migration 0011_migrate_price_categories.py:
# python manage.py makemigrations main_app --name migrate_price_categories --empty
# Do not migrate yet! First create functions in 0011_migrate_price_categories.py as follows:

from django.db import migrations

def set_price_category(apps, schema_editor):

    Item = apps.get_model("main_app", "Item")
    all_items = Item.objects.all()

    for item in all_items:
        if item.price <= 10:
            item.rarity = "Rare"
        elif item.price <= 20:
            item.rarity = "Very Rare"
        elif item.price <= 30:
            item.rarity = "Extremely Rare"
        else:
            item.rarity = "Mega Rare"
        item.save()

def unset_price_category(apps, schema_editor):
    Item = apps.get_model("main_app", "Item")
    all_items = Item.objects.all()

    for item in all_items:
        item.rarity = "empty"
        item.save()

# Do not forget to add dependencies and operations into 0011_migrate_price_categories.py
# Double check filenames

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_price_category, reverse_code=unset_price_category)
    ]


# run caller.py to fill data into the db
# migrate and check if the data is filtered as supposed. If not -repair and debug.

# ----------------------------------------------------------------------------------------

# create and migrate Smartphone model
# Repeat steps as described above
# Do not migrate yet! First create functions in 0013_migrate_price_categories_smartphones.py as follows:
#
