from django.shortcuts import render
from Recipe.serializers import FoodSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Food


# Create your views here.


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # def get_list(self, request):
