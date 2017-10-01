from rest_framework import serializers
from main.models import Tag, Task, User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = ('title', 'description', 'creation_date', 'deadline')
    # Foreing key and Many-to-Many relations ????


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('username', 'email', 'date_joined')
