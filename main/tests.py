"""
Module de tests unitaires et d'intégration
pour l'application principale de MonAvesnois.
"""

from django.test import Client, TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_view(self) -> None:
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")
