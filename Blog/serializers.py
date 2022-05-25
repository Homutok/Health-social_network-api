from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Post, Food, Tags, Recipe, Fitness, Nutrients, FoodNutrients


class PostSerializer(ModelSerializer):
    post_author = StringRelatedField(read_only=False)
    post_tags = StringRelatedField(read_only=False, many=True)
    post_recipes = StringRelatedField(read_only=False, many=True)
    post_fitness = StringRelatedField(read_only=False, many=True)
    permission_classes = IsAuthenticatedOrReadOnly

    class Meta:
        model = Post
        fields = '__all__'


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
