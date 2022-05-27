from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Post, Like, Tags
from Comments.serializers import CommentSerializer


class BlogSerializer(ModelSerializer):
    liked = SerializerMethodField()

    def get_liked(self, obj):
        return obj.likes_for_post.count()

    class Meta:
        model = Post
        fields = ['id', 'post_name', 'post_summary', 'liked']


class PostSerializer(ModelSerializer):
    comment = CommentSerializer(many=True, required=False)
    liked = SerializerMethodField()

    def get_liked(self, obj):
        return obj.likes_for_post.count()

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Like
        fields = ['id', 'content_id']
        # fields = '__all__'


class TagSerializer(ModelSerializer):
    # user = StringRelatedField()

    class Meta:
        model = Tags
        # fields = ['id', 'content_id']
        fields = '__all__'
