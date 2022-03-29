from django.test import Client, TestCase
from django.urls import reverse


# Create your tests here.
class AirTrackerTests(TestCase):

    def test_index_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hi mates, nice to work with you")

