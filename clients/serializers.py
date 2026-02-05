from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']
        
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields = ['username', 'email', 'password']
        
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)