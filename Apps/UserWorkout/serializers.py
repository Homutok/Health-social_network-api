from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Workout


class WorkoutSerializer(ModelSerializer):
    exercise = StringRelatedField()

    class Meta:
        model = Workout
        fields = '__all__'
