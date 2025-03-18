from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

    def test_create_task(self):
        response = self.client.post("/api/tasks/", {
            "title": "Test Task",
            "description": "This is a test task",
            "priority": "high",
            "status": "pending"
        })
        self.assertEqual(response.status_code, 201)
