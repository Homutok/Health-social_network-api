from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Food, Recipe
from Nutrients.serializers import FoodNutrientsSerializer


class FoodSerializer(ModelSerializer):
    # nutrients = StringRelatedField()
    food_author = StringRelatedField()
    # nutrients_for_food = FoodNutrientsSerializer(many=True, required=False)

    class Meta:
        model = Food
        fields = '__all__'


class RecipeSerializer(ModelSerializer):
    recipe_foods = StringRelatedField()
    recipe_author = StringRelatedField()

    class Meta:
        model = Recipe
        fields = '__all__'
