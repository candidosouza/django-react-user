from django.test import TestCase
from django.contrib.auth.models import User
from users.serializers import UserSerializer

class UserSerializerIntegrationTestCase(TestCase):

    def setUp(self):
        self.user_data = {
            'first_name': 'Test',
            'last_name': 'User Example',
            'username': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_serializer_create(self):
        data = {
            'fullname': 'Create User Example',
            'username': 'create@example.com',
            'password': 'createpassword'
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'create@example.com')
        self.assertEqual(user.email, 'create@example.com')
        self.assertEqual(user.first_name, 'Create')
        self.assertEqual(user.last_name, 'User Example')

    def test_serializer_update(self):
        new_data = {
            'fullname': 'Updated User Example',
            'username': 'updated@example.com',
            'password': 'updatepassword'
        }
        serializer = UserSerializer(instance=self.user, data=new_data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.username, 'updated@example.com')
        self.assertEqual(updated_user.email, 'updated@example.com')

    def test_serializer_update_partial_data(self):
        new_data = {
            'username': 'updated@example.com',
        }
        serializer = UserSerializer(instance=self.user, data=new_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.username, 'updated@example.com')
        self.assertEqual(updated_user.email, 'updated@example.com')

    def test_serializer_invalid_data(self):
        invalid_data = {
            'username': '',  # Required field
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_empty_data(self):
        empty_data = {}
        serializer = UserSerializer(data=empty_data)
        self.assertFalse(serializer.is_valid())
