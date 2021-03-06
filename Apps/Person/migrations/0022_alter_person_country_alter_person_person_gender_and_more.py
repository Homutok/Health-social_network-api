# Generated by Django 4.0.1 on 2022-06-16 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Person', '0021_personhealth_person_dream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужчина'), ('female', 'Женщина'), ('other', 'Другие')], default='other', help_text='Половая принадлежность', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ForeignKey(default=30, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_for_user', to='Person.personphoto'),
        ),
        migrations.AlterField(
            model_name='person',
            name='place_of_study',
            field=models.CharField(blank=True, db_index=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.CharField(blank=True, db_index=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='public_user_info', to=settings.AUTH_USER_MODEL),
        ),
    ]
