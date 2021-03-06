# Generated by Django 4.0.1 on 2022-04-04 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0003_alter_person_person_photo'),
        ('Blog', '0006_rename_person_id_post_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrients',
            old_name='rank',
            new_name='nutrient_rank',
        ),
        migrations.RenameField(
            model_name='nutrients',
            old_name='unitName',
            new_name='nutrient_unitName',
        ),
        migrations.AddField(
            model_name='fitness',
            name='fitness_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fitness_for_user', to='Person.person'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='food_for_user', to='Person.person'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='recipe_for_user', to='Person.person'),
        ),
    ]
