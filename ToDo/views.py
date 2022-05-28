from rest_framework import generics
from .models import ToDoTask
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated


class ToDoViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ToDoSerializer

    def get_queryset(self):
        user = self.request.user
        return ToDoTask.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(
            task_author=self.request.user
        )
