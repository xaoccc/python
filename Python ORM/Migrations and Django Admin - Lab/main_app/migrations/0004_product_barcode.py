# Generated by Django 4.2.6 on 2023-10-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20231018_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
