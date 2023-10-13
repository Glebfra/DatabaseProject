from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import APIElementViewSet

router = DefaultRouter()
router.register('elements', APIElementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
