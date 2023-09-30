from django.test import TestCase
from django.contrib.auth.models import User
from .models import CustomUser

class TestCustomUserModel(TestCase):
    def test_create_custom_user(self):
        user = User.objects.create(username='testuser', password='testpassword')
        custom_user = CustomUser.objects.get(user=user)

        self.assertEqual(custom_user.user, user)
        self.assertEqual(custom_user.display_name, user.username)
        self.assertEqual(custom_user.account_type, 'student')

    def test_update_custom_user(self):
        user = User.objects.create(username='testuser', password='testpassword')
        custom_user = CustomUser.objects.get(user=user)

        custom_user.display_name = 'New Display Name'
        custom_user.save()

        updated_custom_user = CustomUser.objects.get(user=user)
        self.assertEqual(updated_custom_user.display_name, 'New Display Name')
