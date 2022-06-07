from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Diet


class DietSerializer(ModelSerializer):

    class Meta:
        model = Diet
        fields = '__all__'
