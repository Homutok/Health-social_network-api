# Generated by Django 4.0.1 on 2022-05-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0007_alter_food_food_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_preview',
            field=models.ImageField(null=True, upload_to='article/food_photo'),
        ),
    ]
