# Generated by Django 4.2.6 on 2023-10-17 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
