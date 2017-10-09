from django.test import TestCase
from django.db.utils import IntegrityError

from tortoise.main.models.user import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="will", email="will@example.com", password='foo123')

    def test_user_case_insensitive(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username="WILL", email="will2@example.com", password='foo123')
