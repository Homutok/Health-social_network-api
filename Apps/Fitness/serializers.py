from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Fitness


class FitnessSerializer(ModelSerializer):

    class Meta:
        model = Fitness
        # fields = ['comment_post', 'comment_text']
        fields = '__all__'
