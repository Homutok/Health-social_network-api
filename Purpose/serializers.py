from rest_framework.serializers import ModelSerializer
from .models import Purposes


class PurposeSerializer(ModelSerializer):
    class Meta:
        model = Purposes
        fields = '__all__'
