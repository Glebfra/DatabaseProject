from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Carousel
from .serializers import CarouselSerializer


# Create your views here.
class APICarouselViewSet(ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
