# Generated by Django 4.2.6 on 2023-11-08 15:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_foodcriticrestaurantreview_regularrestaurantreview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcriticrestaurantreview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='regularrestaurantreview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.CreateModel(
            name='MenuReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.menu')),
            ],
            options={
                'verbose_name': 'Menu Review',
                'verbose_name_plural': 'Menu Reviews',
                'ordering': ['-rating'],
                'indexes': [models.Index(fields=['menu'], name='main_app_menu_review_menu_id')],
                'unique_together': {('reviewer_name', 'menu')},
            },
        ),
    ]
