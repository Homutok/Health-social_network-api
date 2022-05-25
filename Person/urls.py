from django.urls import path
from rest_framework import routers
from Person.views import PersonViewSet

router = routers.DefaultRouter()
router.register('Person', PersonViewSet)

urlpatterns = router.urls