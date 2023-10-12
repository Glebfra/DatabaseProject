from django.urls import path

from .views import ElementList

urlpatterns = [
    path('elements/', ElementList.as_view(), name='element_list')
]
