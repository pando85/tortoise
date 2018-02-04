from django.core.exceptions import ValidationError
from django.db import models

from .user import User
from .tag import Tag


class Task(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=500, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name='tasks_ownership')
    members = models.ManyToManyField(
        User, related_name='tasks_membership', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def clean(self):
        if self.deadline:
            if self.deadline <= self.creation_date:
                raise ValidationError(
                    'Deadline specified is setted before creation date')
