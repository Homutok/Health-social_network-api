# Generated by Django 4.0.1 on 2022-05-28 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0007_alter_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
    ]
