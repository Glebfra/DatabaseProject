from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Element
from .serializers import ElementSerializer


class ElementList(generics.ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            name=self.request.data['name'],
            symbol=self.request.data['symbol']
        )
