from rest_framework import serializers
from .models import UUID

class UuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUID
        fields = ('created', 'uuid')
        read_only_fields = ('created', 'uuid')