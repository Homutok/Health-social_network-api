from datetime import datetime

from rest_framework.relations import PrimaryKeyRelatedField
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Person, PersonPhoto, PersonAchievement, PersonHealth
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

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CreateUserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            date_joined=datetime.now()
        )
        profile = Person.create_profile(self, user)
        return user

    class Meta:
        model = User
        fields = '__all__'


class AchievementsSerializer(ModelSerializer):
    achievement_data = StringRelatedField()

    class Meta:
        model = PersonAchievement
        fields = '__all__'


class HealthSerializer(ModelSerializer):
    class Meta:
        model = PersonHealth
        fields = '__all__'
