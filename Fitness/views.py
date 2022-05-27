from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Fitness
from .serializers import FitnessSerializer
from rest_framework.viewsets import ModelViewSet


class FitnessViewList(ModelViewSet):
    search_fields = ['fitness_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer
