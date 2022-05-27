from rest_framework import generics
from .models import Diet
from .serializers import DietSerializer
from rest_framework.permissions import IsAuthenticated


class DietViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DietSerializer

    def get_queryset(self):
        user = self.request.user
        return Diet.objects.filter(user=user)