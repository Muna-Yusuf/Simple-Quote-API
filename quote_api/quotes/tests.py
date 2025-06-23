from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class QuoteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post_valid_quote(self):
        response = self.client.post("/quotes/", {
            "text": "Hard work beats talent when talent fails to work hard.",
            "author": "Kevin Durant"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("data", response.data)
        self.assertEqual(response.data["message"], "Quote added successfully")

    def test_post_invalid_quote(self):
        response = self.client.post("/quotes/", {
            "text": "Short",
            "author": ""
        }, format="json")
        self.assertEqual(response.status_code, 400)