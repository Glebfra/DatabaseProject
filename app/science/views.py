from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import get_user_model

from .models import Element, PhaseDiagram, SaturationData, Storage
from .serializers import ElementSerializer, PhaseDiagramSerializer, SaturationDataSerializer, StorageSerializer


class APIElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        name = self.request.query_params.get('name')
        symbol = self.request.query_params.get('symbol')
        user = self.request.query_params.get('user')

        queryset = Element.objects.all()
        if name is not None:
            queryset = queryset.filter(name=name)
        if symbol is not None:
            queryset = queryset.filter(symbol=symbol)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset


class APISaturationDataViewSet(ModelViewSet):
    queryset = SaturationData.objects.all()
    serializer_class = SaturationDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.query_params.get('user')
        element = self.request.query_params.get('element')
        temperature = self.request.query_params.get('temperature')
        pressure = self.request.query_params.get('pressure')
        density = self.request.query_params.get('density')

        queryset = SaturationData.objects.all().order_by('temperature')
        if user is not None:
            queryset = queryset.filter(user=user)
        if element is not None:
            queryset = queryset.filter(element=element)
        if temperature is not None:
            queryset = queryset.filter(temperature=temperature)
        if pressure is not None:
            queryset = queryset.filter(pressure=pressure)
        if density is not None:
            queryset = queryset.filter(density=density)
        return queryset


class APIPhaseDiagramDataViewSet(ModelViewSet):
    queryset = PhaseDiagram.objects.all()
    serializer_class = PhaseDiagramSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        user = self.request.query_params.get('user')
        element = self.request.query_params.get('element')
        temperature = self.request.query_params.get('temperature')
        pressure = self.request.query_params.get('pressure')
        density = self.request.query_params.get('density')

        queryset = PhaseDiagram.objects.all().order_by('temperature', 'pressure')
        if user is not None:
            queryset = queryset.filter(user=user)
        if element is not None:
            queryset = queryset.filter(element=element)
        if temperature is not None:
            queryset = queryset.filter(temperature=temperature)
        if pressure is not None:
            queryset = queryset.filter(pressure=pressure)
        if density is not None:
            queryset = queryset.filter(density=density)
        return queryset


class APIStorageViewSet(ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        query = self.request.query_params.get('query')

        queryset = Storage.objects.all()
        queryset.filter(user=self.request.user)
        if query is not None:
            queryset = queryset.filter(query=query)
        return queryset
