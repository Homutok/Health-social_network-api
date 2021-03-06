# Generated by Django 4.0.1 on 2022-06-05 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Person', '0019_alter_personhealth_persons_data_personachievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personachievement',
            name='persons_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievement_for_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
