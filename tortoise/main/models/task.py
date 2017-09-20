from django.core.exceptions import ValidationError
from django.db import models

from tortoise.main.models.user import User
from tortoise.main.models.tag import Tag


class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    owner = models.ForeignKey(User)
    usersgroup = models.ManyToManyField(User)
    tags = models.ManyToManyField(Tag, blank=True)

    def clean(self):
        if self.deadline <= self.creation_date:
            raise ValidationError(
                _('Deadline specified is setted before creation date'))
