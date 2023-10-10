from rest_framework import serializers

from .models import Element


class ModelSerializer(serializers.Serializer):
    class Meta:
        model = Element
        fields = ['id', 'user', 'name']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
