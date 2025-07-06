from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):

    def test_view(self):
        path = reverse('HomeView')
        response = self.client.get(path)
        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/greeting.html')


