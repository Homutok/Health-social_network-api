# Generated by Django 4.0.1 on 2022-05-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0002_fitness_fitness_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitness',
            name='fitness_preview',
            field=models.ImageField(null=True, upload_to='fit_photo'),
        ),
    ]