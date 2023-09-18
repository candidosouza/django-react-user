from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class UserViewSetIntegrationTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'first_name': 'Test',
            'last_name': 'User Example',
            'username': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        new_user_data = {
            'fullname': 'New User',
            'username': 'newuser@example.com',
            'password': 'newpassword',
        }
        response = self.client.post('/api/users/', new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_user = User.objects.get(username=new_user_data['username'])
        self.assertEqual(created_user.first_name, 'New')
        self.assertEqual(created_user.last_name, 'User')

    def test_update_user(self):
        updated_data = {
            'fullname': 'Updated User',
            'username': 'updated@example.com',
            'password': 'updatedpassword',
        }
        response = self.client.put(f'/api/users/{self.user.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, updated_data['username'])
        self.assertEqual(updated_user.email, updated_data['username'])

    def test_partial_update_user(self):
        partial_data = {
            'username': 'updated@example.com',
            'password': 'testpassword'
        }
        response = self.client.patch(f'/api/users/{self.user.id}/', partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        partial_user = User.objects.get(id=self.user.id)
        self.assertEqual(partial_user.username, partial_data['username'])
        self.assertEqual(partial_user.email, partial_data['username'])

    def test_invalid_user_data(self):
        invalid_data = {
            'username': '',  # Required field
        }
        response = self.client.post('/api/users/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_get_user_list_with_pagination(self):
        for i in range(10):
            User.objects.create_user(
                username=f'user{i}@example.com',
                password=f'password{i}'
            )

        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(response.data['count'], 11)
        self.assertEqual(len(response.data['results']), 11)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_get_user_detail(self):
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])

    def test_delete_user(self):
        response = self.client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
