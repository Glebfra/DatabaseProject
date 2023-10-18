from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import APIElementViewSet, APIPhaseDiagramDataViewSet, APISaturationDataViewSet, APIStorageViewSet

router = DefaultRouter()
router.register('elements', APIElementViewSet)
router.register('saturation', APISaturationDataViewSet)
router.register('phase_diagram', APIPhaseDiagramDataViewSet)
router.register('storage', APIStorageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
