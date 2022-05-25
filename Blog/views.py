from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Post, Food
from .serializers import PostSerializer, FoodSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # def get_list(self, request):


