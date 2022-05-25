from django.db import models
from Person.models import Person


class Post(models.Model):
    post_name = models.CharField(max_length=100, db_index=True)
    post_summary = models.CharField(max_length=10000, db_index=True)
    post_author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='post_for_user')
    post_date = models.DateField(null=True, blank=True)
    post_tags = models.ManyToManyField('Tags')
    post_recipes = models.ManyToManyField('Recipe')
    post_fitness = models.ManyToManyField('Fitness')

    def __str__(self):
        return self.post_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.tag_name


class Fitness(models.Model):
    fitness_name = models.CharField(max_length=100, db_index=True)
    fitness_kcal = models.IntegerField(null=True, blank=True)
    fitness_time = models.IntegerField(null=True, blank=True)
    fitness_summary = models.CharField(max_length=200, db_index=True)
    fitness_present = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100, null=True,
                                        blank=True)
    fitness_author = models.ForeignKey(Person, on_delete=models.PROTECT, default=1, related_name='fitness_for_user')

    def __str__(self):
        return self.fitness_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, db_index=True)
    recipe_time = models.IntegerField(null=True, blank=True)
    recipe_summary = models.CharField(max_length=1000, db_index=True)
    recipe_foods = models.ManyToManyField('Food')
    recipe_author = models.ForeignKey(Person, on_delete=models.PROTECT, default=1, related_name='recipe_for_user')

    def __str__(self):
        return self.recipe_name


class Food(models.Model):
    food_name = models.CharField(max_length=1000, db_index=True)
    food_summary = models.CharField(null=True, max_length=500, db_index=True)
    food_ingredient_summary = models.CharField(null=True, max_length=500, db_index=True)
    food_author = models.ForeignKey(Person, on_delete=models.PROTECT, default=1, related_name='food_for_user')

    def __str__(self):
        return self.food_name


class Nutrients(models.Model):
    nutrient_name = models.CharField(max_length=1000, db_index=True)
    nutrient_unitName = models.CharField(max_length=1000, db_index=True)
    nutrient_rank = models.CharField(null=True, max_length=100, db_index=True)

    def __str__(self):
        return str(self.nutrient_name) + "[" + str(self.id) + "]"


class FoodNutrients(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT, null=True, related_name='nutrients_for_food')
    amount = models.FloatField(null=True, blank=True)
    nutrientInfo = models.ForeignKey(Nutrients, on_delete=models.PROTECT, null=True, related_name='nutrients_for_food')

    def __str__(self):
        return str(self.nutrientInfo.nutrient_name) + " " + str(self.amount) + " " + str(
            self.nutrientInfo.nutrient_unitName)
