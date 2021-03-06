# Generated by Django 4.0.1 on 2022-04-04 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0003_alter_person_person_photo'),
        ('Blog', '0009_remove_recipe_recipe_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='recipe_for_user', to='Person.person'),
        ),
    ]
