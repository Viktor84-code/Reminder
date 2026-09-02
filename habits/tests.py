from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Habit


class HabitModelTest(TestCase):
    def test_create_habit(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        habit = Habit.objects.create(
            user=user,
            place="Дом",
            time="08:00:00",
            action="Зарядка",
            is_pleasant=False,
            periodicity=1,
            duration=60,
            is_public=False,
        )
        self.assertEqual(habit.action, "Зарядка")
        self.assertEqual(habit.user, user)


class HabitAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_create_habit(self):
        data = {
            "place": "Дом",
            "time": "08:00:00",
            "action": "Зарядка",
            "is_pleasant": False,
            "periodicity": 1,
            "duration": 60,
            "is_public": False,
        }
        response = self.client.post("/api/habits/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["action"], "Зарядка")

    def test_list_habits(self):
        Habit.objects.create(
            user=self.user, place="Дом", time="08:00:00", action="Зарядка", duration=60
        )
        response = self.client.get("/api/habits/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

    def test_public_habits(self):
        Habit.objects.create(
            user=self.user,
            place="Дом",
            time="08:00:00",
            action="Публичная",
            duration=60,
            is_public=True,
        )
        response = self.client.get("/api/habits/public/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

    def test_update_habit(self):
        habit = Habit.objects.create(
            user=self.user, place="Дом", time="08:00:00", action="Зарядка", duration=60
        )
        response = self.client.patch(
            f"/api/habits/{habit.id}/", {"action": "Новая зарядка"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["action"], "Новая зарядка")

    def test_delete_habit(self):
        habit = Habit.objects.create(
            user=self.user, place="Дом", time="08:00:00", action="Зарядка", duration=60
        )
        response = self.client.delete(f"/api/habits/{habit.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)
