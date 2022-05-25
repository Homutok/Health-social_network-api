from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, db_index=True)
    recipe_time = models.IntegerField(null=True, blank=True)
    recipe_summary = models.CharField(max_length=1000, db_index=True)
    recipe_foods = models.ManyToManyField('Food')
    recipe_author = models.ForeignKey(User, on_delete=models.PROTECT, default=1, related_name='recipe_for_user')

    def __str__(self):
        return self.recipe_name


class Food(models.Model):
    food_name = models.CharField(null=True,max_length=1000, db_index=True)
    food_summary = models.CharField(null=True, max_length=500, db_index=True)
    food_ingredient_summary = models.CharField(null=True, max_length=500, db_index=True)
    food_author = models.ForeignKey(User, on_delete=models.PROTECT, default=1, related_name='food_for_user')
    food_preview = models.ImageField(null=True)

    def __str__(self):
        return self.food_name
