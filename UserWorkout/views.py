from rest_framework import generics
from .models import Workout
from .serializers import WorkoutSerializer
from rest_framework.permissions import IsAuthenticated


class WorkoutViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        user = self.request.user
        return Workout.objects.filter(user=user)