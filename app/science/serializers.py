from rest_framework import serializers

from .models import Element, PhaseDiagram, SaturationData, Storage


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


class PhaseDiagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhaseDiagram
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        phase = PhaseDiagram(**validated_data)
        phase.save()
        return phase

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.pressure = validated_data.get('pressure', instance.pressure)
        instance.density = validated_data.get('density', instance.density)
        instance.save()


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        storage = Storage(**validated_data)
        storage.save()
        return storage

    def update(self, instance, validated_data):
        instance.values = validated_data.get('values', instance.values)
        instance.query = validated_data.get('query', instance.query)
        instance.save()
