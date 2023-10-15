from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Element, SaturationData


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        element = Element(**validated_data)
        element.save()
        return element

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.save()
        return instance


class SaturationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaturationData
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        saturation = SaturationData(**validated_data)
        saturation.save()
        return saturation

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.pressure = validated_data.get('pressure', instance.pressure)
        instance.density = validated_data.get('density', instance.density)
