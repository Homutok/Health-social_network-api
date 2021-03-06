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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Blog.views import PostLikeView, BlogViewList, BlogViewDetail, LikeViewSet, TagViewSet
from Favourite.views import FavouriteViewList
from Fitness.views import FitnessViewList
from ToDo.views import ToDoViewSet, ToDoDetailViewSet
from UserDiet.views import DietViewSet
from UserWorkout.views import WorkoutViewSet, WorkoutDeleteViewSet
from Person.views import CreateUserViewSet, MyUserHealthLast, MyUserDetail, MyUserAchievements, UserViewSet, UserDetail, PhotoListView, MyUserHealthList, UserDetailUpdate
from Recipe.views import FoodViewSet
from Nutrients.views import FoodNutrientsViewList
from backend import settings
from Comments.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'Likes', LikeViewSet)
router.register(r'Tags', TagViewSet)
router.register(r'Fitness', FitnessViewList)
router.register(r'Comments', CommentViewSet, basename='Comment')

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
    path('api/Image/', PhotoListView.as_view()),
]
urlpatterns += [
    path('api/Register/', CreateUserViewSet.as_view()),
    path('api/MyProfile/', MyUserDetail.as_view()),
    path('api/MyAchievments/', MyUserAchievements.as_view()),
    path('api/MyHealth/', MyUserHealthList.as_view()),
    path('api/MyHealthLast/', MyUserHealthLast.as_view()),
    path('api/Profile/', UserViewSet.as_view()),
    path('api/Profile/<int:pk>/', UserDetail.as_view()),
    path('api/ProfileUpdate/<int:pk>/', UserDetailUpdate.as_view()),
]
urlpatterns += [
    path('api/ToDo/', ToDoViewSet.as_view()),
    path('api/ToDo/<int:pk>/', ToDoDetailViewSet.as_view()),
]
urlpatterns += [
    path('api/Favourite/', FavouriteViewList.as_view()),
    path('api/Diets/', DietViewSet.as_view()),
]
urlpatterns += [
    path('api/Workouts/', WorkoutViewSet.as_view()),
    path('api/WorkoutsDelete/<int:pk>/', WorkoutDeleteViewSet.as_view()),
]
urlpatterns += [
    path('api/Food/', FoodViewSet.as_view()),
    path('api/FoodNutrient/', FoodNutrientsViewList.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)