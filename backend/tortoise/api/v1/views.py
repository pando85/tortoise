from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tortoise.api.v1.serializers import (
    TagSerializer, TaskSerializer, UserSerializer)
from tortoise.main.models.user import User
from tortoise.main.models.tag import Tag
from tortoise.main.models.task import Task

from .permissions import IsOwnerOrReadOnly, IsItself


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsItself, )

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.none()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return Task.objects.filter(
            Q(owner=self.request.user) | Q(members=self.request.user))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
