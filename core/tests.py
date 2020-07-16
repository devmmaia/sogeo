from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User


class APITests(APITestCase):
    def test_list_user_status_ok(self):
        """
        Ensure we got a status 200 when listing users
        """
        url = reverse("user-list")

        response = self.client.get(url, data=None, format="json")
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        """
        Creating some users for testing.
        """
        self.user1 = User.objects.create_user(
            username="johnlennon", password="aA12#$sd", about="Imagine"
        )
        self.user2 = User.objects.create_user(
            username="howardlevy", password="aA12#$sd"
        )

    def test_list_user_returns_all(self):
        """
        Assert all users are listed.
        """
        url = reverse("user-list")
        response = self.client.get(url, data=None, format="json")
        self.assertEqual(len(response.data), 2)

    def test_if_get_user_returns_ok(self):
        kwargs = {"pk": self.user1.id}
        url = reverse("user-detail", kwargs=kwargs)
        response = self.client.get(url, data=None, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["about"], "Imagine")
