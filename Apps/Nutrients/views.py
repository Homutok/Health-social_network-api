from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import FoodNutrients
from .serializers import FoodNutrientsSerializer
from rest_framework.viewsets import ModelViewSet


class FoodNutrientsViewList(generics.ListAPIView):
    queryset = FoodNutrients.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=food__id']
    pagination_class = None
    serializer_class = FoodNutrientsSerializer
