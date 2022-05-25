from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Purposes
from .serializers import PurposeSerializer


class PurposeViewSet(ModelViewSet):
    queryset = Purposes.objects.all()
    serializer_class = PurposeSerializer
