from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    birth_name = serializers.CharField(max_length=200)
    image = serializers.URLField()
    # bio = serializers.TextField(null= True, blank = True)
    
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)