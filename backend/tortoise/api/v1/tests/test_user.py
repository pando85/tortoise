
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from tortoise.main.models.user import User
from tortoise.api.v1.views import UserViewSet


class CreateUserTest(APITestCase):
    def setUp(self):
        self.url = reverse('v1:user-list')
        self.data = {'username': 'foo', 'password': 'foo'}

    def test_can_create_user(self):
        """
        Ensure we can create a new user.
        """
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, self.data['username'])

class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='foo', password='foo')
        self.client.login(username='foo', password='foo')

    def test_change_user_password(self):
        """
        Ensure we can change user password
        """
        data = {'username': 'foo', 'password': 'boo'}
        url = reverse('v1:user-detail', args=[data['username']])
        response = self.client.put(url , data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PermissionsUserTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='foo', password='foo')
        self.user2 = User.objects.create_user(username='boo', password='boo')
        self.client.login(username='foo', password='foo')

    def test_get_own_user_detail(self):
        """
        Ensure we can get own user details
        """
        url = reverse('v1:user-detail', args=['foo'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('foo', response.data['username'])

    def test_not_get_other_user_details(self):
        """
        Ensure we can't get other user details
        """
        url = reverse('v1:user-detail', args=['boo'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_not_change_other_user_password(self):
        """
        Ensure we can't change other user password
        """
        data = {'username': 'boo', 'password': 'foo'}
        url = reverse('v1:user-detail', args=[data['username']])
        response = self.client.put(url , data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
