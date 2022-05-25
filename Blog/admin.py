from django.contrib import admin
from .models import Post, Tags, Fitness, Recipe, Food, FoodNutrients, Nutrients

admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Fitness)
admin.site.register(Recipe)
admin.site.register(Food)
admin.site.register(FoodNutrients)
admin.site.register(Nutrients)
