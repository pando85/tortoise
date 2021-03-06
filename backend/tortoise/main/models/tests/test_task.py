
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.test import TestCase

from tortoise.main.models.user import User
from tortoise.main.models.task import Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="will", email="will@example.com")
        Task.objects.create(name="Buy soap", owner=self.user)

    def test_task_created(self):
        example_task = Task.objects.get(name="Buy soap")
        example_task.full_clean()
        self.assertEqual(example_task.name, "Buy soap")

    def test_task_invalid_deadline(self):
        now = timezone.now()
        with self.assertRaises(ValidationError):
            a = Task.objects.create(
                name="Test deadline", owner=self.user, deadline=now)
            a.full_clean()
