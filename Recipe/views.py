from rest_framework import generics, filters
from Recipe.serializers import FoodSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import StandardResultsSetPagination
from .models import Food


class FoodViewSet(generics.ListAPIView):
    queryset = Food.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = FoodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['food_name']

    # def get_list(self, request):
