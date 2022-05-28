"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Blog.views import PostLikeView, BlogViewList, BlogViewDetail, LikeViewSet, TagViewSet
from Favourite.views import FavouriteViewList
from Fitness.views import FitnessViewList
from ToDo.views import ToDoViewSet
from UserDiet.views import DietViewSet
from UserWorkout.views import WorkoutViewSet
from Person.views import MyUserDetail, UserViewSet, UserDetail

router = routers.DefaultRouter()
router.register(r'Likes', LikeViewSet)
router.register(r'Tags', TagViewSet)
router.register(r'Fitness', FitnessViewList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += [
    path('api/Blog/', BlogViewList.as_view()),
    path('api/Blog/<int:pk>/', BlogViewDetail.as_view()),
]
urlpatterns += [
    path('api/Liked/<int:pk>/', PostLikeView.as_view()),
]
urlpatterns += [
    path('api/MyProfile/', MyUserDetail.as_view()),
    path('api/Profile/', UserViewSet.as_view()),
    path('api/Profile/<int:pk>/', UserDetail.as_view()),
]
urlpatterns += [
    path('api/Favourite/', FavouriteViewList.as_view()),
    path('api/ToDO/', ToDoViewSet.as_view()),
    path('api/Diets/', DietViewSet.as_view()),
    path('api/Workouts/', WorkoutViewSet.as_view()),
    # path('api/Blog/<int:pk>/', BlogViewDetail.as_view()),
]
