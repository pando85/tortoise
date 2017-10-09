from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tortoise.api.serializers import (TagSerializer,
    TaskSerializer, UserSerializer)
from tortoise.main.models.user import User
from tortoise.main.models.tag import Tag
from tortoise.main.models.task import Task

from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.none()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return Task.objects.filter(
            Q(owner=self.request.user) | Q(members=self.request.user))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
