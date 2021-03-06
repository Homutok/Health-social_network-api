# Generated by Django 4.0.1 on 2022-06-21 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0007_alter_fitness_fitness_preview_and_more'),
        ('UserWorkout', '0004_alter_workout_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise_from_blog', to='Fitness.fitness'),
        ),
    ]
