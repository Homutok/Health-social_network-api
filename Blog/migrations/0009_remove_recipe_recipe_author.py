# Generated by Django 4.0.1 on 2022-04-04 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_fitness_fitness_author_alter_food_food_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_author',
        ),
    ]
