from rest_framework import serializers

from .models import Element


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
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
