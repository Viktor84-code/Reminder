from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        data = {
            "username": "newuser",
            "password": "newpass123",
            "email": "new@mail.com"
        }
        response = self.client.post("/api/auth/register/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login(self):
        User.objects.create_user(username="testuser", password="testpass")
        data = {
            "username": "testuser",
            "password": "testpass"
        }
        response = self.client.post("/api/auth/token/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_invalid(self):
        data = {
            "username": "wronguser",
            "password": "wrongpass"
        }
        response = self.client.post("/api/auth/token/", data, format="json")
        self.assertEqual(response.status_code, 401)
