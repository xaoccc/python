# Generated by Django 3.2.7 on 2023-11-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_foodcriticrestaurantreview_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcriticrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Food Critic Review', 'verbose_name_plural': 'Food Critic Reviews'},
        ),
    ]
