from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import APIElementViewSet, APISaturationDataViewSet

router = DefaultRouter()
router.register('elements', APIElementViewSet)
router.register('saturation', APISaturationDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
