# Generated by Django 4.0.1 on 2022-01-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purpose', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purposes',
            old_name='persons_data',
            new_name='person_data',
        ),
    ]
