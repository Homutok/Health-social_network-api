# Generated by Django 4.0.1 on 2022-05-26 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fitness', '0002_fitness_fitness_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1, help_text='День недели', max_length=1)),
                ('exercise', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_exercise', to='Fitness.fitness')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user_workout', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]