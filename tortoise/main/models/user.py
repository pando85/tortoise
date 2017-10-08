from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_by_natural_key(self, username):
        return self.get(username__iexact = username)
