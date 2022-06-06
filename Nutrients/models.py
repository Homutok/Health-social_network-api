from django.db import models
from Recipe.models import Food


class Nutrients(models.Model):
    nutrient_name = models.CharField(max_length=1000, db_index=True)
    nutrient_unitName = models.CharField(max_length=1000, db_index=True)
    nutrient_rank = models.CharField(null=True, max_length=100, db_index=True)

    def __str__(self):
        return str(self.nutrient_name) + "[" + str(self.id) + "]"


class FoodNutrients(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, related_name='nutrients_for_food')
    amount = models.FloatField(null=True, blank=True)
    nutrientInfo = models.ForeignKey(Nutrients, on_delete=models.PROTECT, null=True, related_name='nutrients')

    def __str__(self):
        return str(self.nutrientInfo.nutrient_name) + " " + str(self.amount) + " " + str(
            self.nutrientInfo.nutrient_unitName)