from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import get_user_model

from .models import Element
from .serializers import ElementSerializer


class APIElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=get_user_model())
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
