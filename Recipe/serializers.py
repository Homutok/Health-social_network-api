from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import  Food
from Nutrients.serializers import FoodNutrientsSerializer


class FoodSerializer(ModelSerializer):
    nutrients = StringRelatedField()
    food_author = StringRelatedField()
    nutrients_for_food = FoodNutrientsSerializer(many=True, required=False)

    class Meta:
        model = Food
        fields = '__all__'
