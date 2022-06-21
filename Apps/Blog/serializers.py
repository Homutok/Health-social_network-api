from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Post, Like, Tags
from Comments.serializers import CommentSerializer
from rest_framework.relations import PrimaryKeyRelatedField


class LikeSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Like
        fields = '__all__'


class LikeCreateSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Like
        fields = ['id', 'content_id']


class TagSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Tags
        # fields = ['id', 'content_id']
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    liked = SerializerMethodField()
    likes_for_post = LikeSerializer(many=True, required=False)
    post_tags = TagSerializer(many=True, required=False)
    #
    # def create(self, validated_data):
    #     tags_data = validated_data.pop('post_tags', None)
    #     post = Post.objects.create(**validated_data)
    #     for tag in tags_data.split(','):
    #         tag = Tags.objects.get(id=tag)
    #         post.post_tags.add(tag)
    #     return post

    def get_liked(self, obj):
        return obj.likes_for_post.count()

    class Meta:
        model = Post
        fields = ['id', 'post_name', 'post_summary', 'liked', 'post_image', 'post_type', 'likes_for_post', 'post_tags']


class PostSerializer(ModelSerializer):
    comment = CommentSerializer(many=True, required=False)
    liked = SerializerMethodField()
    likes_for_post = LikeSerializer(many=True, required=False)
    post_tags = TagSerializer(many=True)

    def get_liked(self, obj):
        return obj.likes_for_post.count()


    class Meta:
        model = Post
        fields = '__all__'
