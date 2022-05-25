from django.urls import path
from rest_framework import routers
from Purpose.views import PurposeViewSet

router = routers.DefaultRouter()
router.register('Purpose', PurposeViewSet)

urlpatterns = router.urls