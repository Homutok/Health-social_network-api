# Generated by Django 4.0.1 on 2022-05-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutrient_name', models.CharField(db_index=True, max_length=1000)),
                ('nutrient_unitName', models.CharField(db_index=True, max_length=1000)),
                ('nutrient_rank', models.CharField(db_index=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodNutrients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nutrients_for_food', to='Recipe.food')),
                ('nutrientInfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nutrients_for_food', to='Nutrients.nutrients')),
            ],
        ),
    ]
