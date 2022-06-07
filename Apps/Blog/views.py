from .models import Post, Like, Tags
from .serializers import PostSerializer, BlogSerializer, LikeSerializer, TagSerializer
import datetime
from rest_framework import permissions, filters, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render


class ResponseCode:
    ALL = 'all'
    FITNESS = 'fitness'
    DIET = 'diet'


class BlogViewList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(
            post_author=self.request.user,
            post_date=datetime.datetime.now())

    def get_queryset(self):
        queryset = Post.objects.all()
        type = self.request.GET.get('type')
        if type is not None:
            queryset = queryset.filter(post_type=type)
        return queryset


class BlogViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(ModelViewSet):
    search_fields = ['content_id']
    filter_backends = (filters.SearchFilter,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class PostLikeView(APIView):
    serializer_class = LikeSerializer
    pagination_class = None

    def get(self, request, pk, *args, **kwargs):
        items = get_object_or_404(Like, user=self.request.user, content_id=self.kwargs.get('pk'))
        return Response(data={"detail": True})


class TagViewSet(ModelViewSet):
    search_fields = ['tag_name']
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    queryset = Tags.objects.all()
    serializer_class = TagSerializer