# Generated by Django 4.0.1 on 2022-05-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0001_initial'),
        ('Blog', '0013_remove_post_post_fitness'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_fitness',
            field=models.ManyToManyField(to='Fitness.Fitness'),
        ),
    ]
