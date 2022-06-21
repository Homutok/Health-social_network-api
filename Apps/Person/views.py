from datetime import datetime

from django.contrib.auth.models import User

from .models import Person, PersonPhoto, PersonAchievement, PersonHealth
from .pagination import StandardWeekResultsSetPagination
from .serializers import PhotoSerializer, PersonSerializer, UserSerializer, AchievementsSerializer, HealthSerializer, \
    CreateUserSerializer, UserUpdateSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class UserViewSet(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CreateUserViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]

    def perform_create(self, serializer):
        serializer.save(date_joined=datetime.now())


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


class UserDetailUpdate(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = UserUpdateSerializer


class MyUserAchievements(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        user = self.request.user
        return PersonAchievement.objects.filter(persons_data=user)


class MyUserHealthList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HealthSerializer
    pagination_class = StandardWeekResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        return PersonHealth.objects.filter(persons_data=user).order_by('-date_of_check')

    def perform_create(self, serializer):
        serializer.save(date_of_check=datetime.today().strftime('%Y-%m-%d'), persons_data=self.request.user)


class MyUserHealthLast(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HealthSerializer

    def get_queryset(self):
        user = self.request.user
        return PersonHealth.objects.filter(persons_data=user).order_by('-id')
