import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


class UserSetup:
    @pytest.fixture
    def super_user(self):
        return User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@example.com',
            is_admin=True,
            is_superuser=True,
            is_staff=True,
        )

    @pytest.fixture
    def low_perm_user(self):
        return User.objects.create_user(
            username='user',
            password='userpass',
            email='user@example.com',
        )

    @pytest.fixture
    def api_client(self):
        return APIClient()
