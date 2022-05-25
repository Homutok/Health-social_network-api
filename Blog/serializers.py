from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Post


class PostSerializer(ModelSerializer):
    post_author = StringRelatedField(read_only=False)
    post_tags = StringRelatedField(read_only=False, many=True)
    post_recipes = StringRelatedField(read_only=False, many=True)
    post_fitness = StringRelatedField(read_only=False, many=True)
    permission_classes = IsAuthenticatedOrReadOnly

    class Meta:
        model = Post
        fields = '__all__'
