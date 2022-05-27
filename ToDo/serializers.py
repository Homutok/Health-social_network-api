from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import ToDoTask


class ToDoSerializer(ModelSerializer):

    class Meta:
        model = ToDoTask
        fields = '__all__'
