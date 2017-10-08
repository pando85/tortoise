from rest_framework import viewsets

from tortoise.api.serializers import (TagSerializer,
    TaskSerializer, UserSerializer)
from tortoise.main.models.user import User
from tortoise.main.models.tag import Tag
from tortoise.main.models.task import Task


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
