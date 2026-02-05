from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']
