# Generated by Django 4.0.1 on 2022-06-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0013_alter_personphoto_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='group_of_study',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='place_of_study',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
    ]
