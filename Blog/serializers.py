from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField
from .models import Post, Like


class PostSerializer(ModelSerializer):
    post_author = StringRelatedField(read_only=False)
    post_tags = StringRelatedField(read_only=False, many=True)

    liked = SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(ModelSerializer):
    # comment = CommentSerializer(many=True, required=False)
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