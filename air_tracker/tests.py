from django.test import Client, TestCase
from django.urls import reverse
from .models import Station_details


# Create your tests here.
class AirTrackerIndexTests(TestCase):

    def test_index_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Station Details")
        self.assertContains(response, "Anderson Drive")
        self.assertContains(response, "Erroll Park")
        self.assertContains(response, "King Street")
        self.assertContains(response, "Market Street 2")
        self.assertContains(response, "Union Street")
        self.assertContains(response, "Wellington Road")
        stations = Station_details.objects.all()
        for station in stations:
            self.assertContains(response, station.site_name)


class AirTrackerDataTests(TestCase):

    def test_data_text(self):
        client = Client()
        response = client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Use the station and date filters here")
