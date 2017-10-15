from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CaseInsensitiveUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if username:
            username = username.lower()

        return super()._create_user(
            username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)


class User(AbstractUser):
    objects = CaseInsensitiveUserManager()
