from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Person, PersonPhoto
from .serializers import PersonSerializer, UserSerializer, PhotoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView


class UserViewSet(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class UserDetail(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PhotoListView(ListAPIView):
    queryset = PersonPhoto.objects.all()
    pagination_class = None
    serializer_class = PhotoSerializer


class MyUserDetail(APIView):
    def get(self, request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)
