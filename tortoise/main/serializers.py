from rest_framework import serializers
from main.models import Tag, Task, User


class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, unique=True)
  

class TaskSerializer(serializers.Serializer):
    title = serializer.CharField(max_length=80)
    description = serializer.CharField(max_length=500, allow_blank=True)
    creation_date = serializer.DateTimeField(auto_now_add=True)
    deadline = serializer.DateTimeField(allow_blank=True, null=True)
    # Foreing key and Many-to-Many relations ????

class UserSerializer(serializers.Serializer):
    username = serializer.CharField(max_length=32, unique=True)
    email = serializer.EmailField(unique=True)
    date_joined = serializer.DateTimeField(auto_now_add=True)
    
