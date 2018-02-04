from rest_framework import serializers

from tortoise.main.models.user import User
from tortoise.main.models.tag import Tag
from tortoise.main.models.task import Task


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'deadline', 'members', 'tags')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = [
            'is_staff', 'is_superuser', 'date_joined', 'last_login',
            'is_active', 'id']
