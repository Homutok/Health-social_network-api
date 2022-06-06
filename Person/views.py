from .models import Person, PersonPhoto, PersonAchievement, PersonHealth
from .pagination import StandardWeekResultsSetPagination
from .serializers import PhotoSerializer, PersonSerializer, UserSerializer, AchievementsSerializer, HealthSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


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


class MyUserAchievements(ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        user = self.request.user
        return PersonAchievement.objects.filter(persons_data=user)


class MyUserHealthList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HealthSerializer
    pagination_class = StandardWeekResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        return PersonHealth.objects.filter(persons_data=user).order_by('-date_of_check')


class MyUserHealthLast(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HealthSerializer

    def get_queryset(self):
        user = self.request.user
        return PersonHealth.objects.filter(persons_data=user).order_by('-id')
