from django.contrib import admin

# Register your models here.
from .models import FoodNutrients, Nutrients

admin.site.register(FoodNutrients)
admin.site.register(Nutrients)
