# Generated by Django 4.0.1 on 2022-06-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('summary', models.CharField(db_index=True, max_length=1000)),
                ('photo', models.FileField(null=True, upload_to='article/achievement_photo')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
