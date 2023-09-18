from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from unittest.mock import Mock
from rest_framework import status

from users.api import UserApiViewSet


class UserViewSetTestCase(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserApiViewSet.as_view({'post': 'create'})

    def test_create_user(self):
        data = {
            'username': 'test@example.com',
            'password': 'testpassword'
        }
        request = self.factory.post('/api/users/', data)

        with self.subTest('Valid Data'):
            response = self.view(request)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        with self.subTest('Invalid Data'):
            # Remova o campo 'username' para tornar os dados inválidos
            invalid_data = data.copy()
            invalid_data.pop('username')
            request = self.factory.post('/api/users/', invalid_data)

            response = self.view(request)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
