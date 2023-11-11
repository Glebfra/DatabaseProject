from rest_framework import serializers

from .models import *


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'
        read_only_fields = []

    def create(self, validated_data):
        model = self.Meta.model(**validated_data)
        model.save()
        return model


class ElementSerializer(BaseSerializer):
    class Meta:
        model = Element
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.save()
        return instance


class SaturationDataSerializer(BaseSerializer):
    class Meta:
        model = SaturationData
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.pressure = validated_data.get('pressure', instance.pressure)
        instance.density = validated_data.get('density', instance.density)


class PhaseDiagramSerializer(BaseSerializer):
    class Meta:
        model = PhaseDiagram
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.pressure = validated_data.get('pressure', instance.pressure)
        instance.density = validated_data.get('density', instance.density)
        instance.save()


class StorageSerializer(BaseSerializer):
    class Meta:
        model = Storage
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def update(self, instance, validated_data):
        instance.values = validated_data.get('values', instance.values)
        instance.query = validated_data.get('query', instance.query)
        instance.save()


class StateSerializer(BaseSerializer):
    class Meta:
        model = State
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.save()
