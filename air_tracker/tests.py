from django.test import Client, TestCase
from django.urls import reverse
from .models import Station_details


# Create your tests here.
class AirTrackerIndexTests(TestCase):

    def test_index_text(self):
        client = Client()
        response = client.get('/')
        stations = Station_details.objects.all()
        """
        for station in stations:
            print(station.site_name)
            self.assertContains(response, station.site_name)
        """
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Station Details")
        self.assertContains(response, "Anderson Drive")
        self.assertContains(response, "Erroll Park")
        self.assertContains(response, "King Street")
        self.assertContains(response, "Market Street 2")
        self.assertContains(response, "Union Street")
        self.assertContains(response, "Wellington Road")
        self.assertTemplateUsed(response, 'air_tracker/home.html')


class AirTrackerDataTests(TestCase):

    def test_data_text(self):
        client = Client()
        response = client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kindly select a station to view data")
        self.assertTemplateUsed(response, 'air_tracker/data.html')

    def test_data_form(self):
        client = Client()
        response = client.post('/data', {'station': 6})
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Wellington Road")

class AirTrackerAirPollutionTests(TestCase):

    def test_air_pollution_text(self):
        client = Client()
        response = client.get('/about-air-pollution')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Air Pollution")
        self.assertContains(response, "Related links")
        self.assertTemplateUsed(response, 'air_tracker/info.html')
