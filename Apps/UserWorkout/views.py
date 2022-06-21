from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework.permissions import IsAuthenticated


class WorkoutViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return Workout.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class WorkoutDeleteViewSet(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return Workout.objects.filter(user=user)
