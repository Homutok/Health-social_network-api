from rest_framework.relations import PrimaryKeyRelatedField
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Person, PersonPhoto
from Blog.serializers import LikeSerializer

from Blog.models import Post


class PhotoSerializer(ModelSerializer):

    class Meta:
        model = PersonPhoto
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    photo = PhotoSerializer()

    class Meta:
        model = Person
        fields = '__all__'


class UserSerializer(ModelSerializer):
    post_for_user = PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    public_user_info = PersonSerializer()
    # photo = PhotoSerializer()
    # likes = LikeSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
