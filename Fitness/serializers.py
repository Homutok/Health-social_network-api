from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import FoodNutrients, Food


class FoodNutrientsSerializer(ModelSerializer):
    nutrientInfo = StringRelatedField()

    class Meta:
        model = FoodNutrients
        fields = '__all__'


class FoodSerializer(ModelSerializer):
    nutrients = StringRelatedField()
    food_author = StringRelatedField()
    nutrients_for_food = FoodNutrientsSerializer(many=True, required=False)

    class Meta:
        model = Food
        fields = '__all__'
