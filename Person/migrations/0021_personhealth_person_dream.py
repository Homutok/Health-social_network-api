# Generated by Django 4.0.1 on 2022-06-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0020_alter_personachievement_persons_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='personhealth',
            name='person_dream',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
