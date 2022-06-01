from django.test import TestCase
from django.urls import reverse


class ConverterTest(TestCase):
    def test_converter_at_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_exchange/convert.html')

    def test_converter_post_request(self):
        response = self.client.post(reverse('convert'), {
            'amount': 1200, 'from_choice': 'EUR', 'to_choice': 'USD'
        })
        self.assertEqual(response.status_code, 200)
