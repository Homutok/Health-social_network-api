from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteViewList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavouriteSerializer

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(user=user)