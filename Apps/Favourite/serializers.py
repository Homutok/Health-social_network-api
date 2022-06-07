from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Favourite


class FavouriteSerializer(ModelSerializer):

    class Meta:
        model = Favourite
        # fields = ['comment_post', 'comment_text']
        fields = '__all__'
