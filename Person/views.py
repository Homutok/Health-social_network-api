from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Person
from .serializers import PersonSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView


class UserViewSet(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class UserDetail(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MyUserDetail(APIView):
    def get(self, request):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)
