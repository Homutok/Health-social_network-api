from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer


# Create your views here.
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(
            comment_author=self.request.user
        )
