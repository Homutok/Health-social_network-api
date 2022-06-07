from rest_framework.viewsets import ModelViewSet
from .models import Purposes
from .serializers import PurposeSerializer
from rest_framework.permissions import IsAuthenticated


class PurposeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PurposeSerializer

    def get_queryset(self):
        user = self.request.user
        return Purposes.objects.filter(user=user)