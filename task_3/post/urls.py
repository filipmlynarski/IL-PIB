from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostHistoryViewSet, PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"history", PostHistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
