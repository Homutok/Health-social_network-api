from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import FoodNutrients


class FoodNutrientsSerializer(ModelSerializer):
    nutrientInfo = StringRelatedField()
    food = StringRelatedField()

    class Meta:
        model = FoodNutrients
        fields = '__all__'
