from django.test import TestCase
from django.contrib.auth.models import User
from users.serializers import UserSerializer

class UserSerializerTestCase(TestCase):

    def setUp(self):
        self.user_data = {
            'fullname': 'Test User Example',
            'username': 'test@example.com',
            'password': 'testpassword'
        }

    def test_serializer_create(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'test@example.com')

    def test_serializer_update(self):
        data = {
            'email': 'test@example.com',
            'username': 'test@example.com',
            'password': 'testpassword'
        }
        user = User.objects.create_user(**data)
        self.assertEqual(user.username, 'test@example.com')
        self.assertEqual(user.email, 'test@example.com')

        updated_data = {
            'username': 'newusername@email.com',
            'password': 'newpassword'
        }
        serializer = UserSerializer(instance=user, data=updated_data, partial=True)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'newusername@email.com')
        self.assertEqual(user.email, 'newusername@email.com')
