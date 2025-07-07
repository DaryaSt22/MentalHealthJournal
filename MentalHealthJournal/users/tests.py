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


# class LoginFormViewTestCase(TestCase):
#
#     def test_list(self):
#         path = reverse('login/')
#         response = self.client.get(path)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertTemplateUsed(response, 'registration/login.html')



class SignUpFormViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('sign_up')

    def tests_signUp_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
