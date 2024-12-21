"""
Module de tests unitaires et d'intégration
pour l'application principale de MonAvesnois.
"""

from django.test import Client, TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    """Tests for the home view."""

    def setUp(self) -> None:
        """Set up test client."""
        self.client = Client()

    def test_home_view(self) -> None:
        """Test that home view returns 200 and uses correct template."""
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/home.html")
        self.assertEqual(response.context["title"], "Accueil")
