# Generated by Django 4.0.1 on 2022-05-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0005_food_recipe_recipe_foods'),
        ('Fitness', '0001_initial'),
        ('Blog', '0015_remove_foodnutrients_food_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(blank=True, choices=[('all', 'Все новости'), ('fitness', 'Занятия спортом'), ('diet', 'Питание ')], default='all', help_text='Тип новостей', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_fitness',
            field=models.ManyToManyField(blank=True, null=True, to='Fitness.Fitness'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_recipes',
            field=models.ManyToManyField(blank=True, null=True, to='Recipe.Recipe'),
        ),
    ]