from django.urls import path
from rest_framework import routers
from Blog.views import PostViewSet, FoodViewSet

router = routers.DefaultRouter()
router.register('Blog', PostViewSet)
router.register('Food', FoodViewSet)

urlpatterns = router.urls
