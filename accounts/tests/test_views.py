from django.test import TestCase, Client
from django.urls import reverse

from .factories import UserFactory


class AuthenticationViewTest(TestCase):
    """
    Tests for `AuthenticationView` class.
    """

    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.url = reverse('accounts:login')
        self.template = 'registration/login.html'

    def test_get_request(self):
        """
        Test view with a GET request.
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)
        self.assertContains(response, 'form')

    def test_post_request_with_valid_username_and_password(self):
        """
        Ensure POST request with a valid `username` & `password`
        login a user.
        """
        self.user.set_password('password')
        self.user.save()
        payload = {
            'username': self.user.username,
            'password': 'password'
        }
        response = self.client.post(self.url, payload)
        self.assertRedirects(response, '/dashboard/')

    def test_post_request_with_valid_email_and_password(self):
        """
        Ensure POST request with a valid `email`  & `password`
        login a user.
        """
        self.user.set_password('password')
        self.user.save()
        payload = {
            'username': self.user.email,
            'password': 'password'
        }
        response = self.client.post(self.url, payload)
        self.assertRedirects(response, '/dashboard/')

    def test_post_request_with_invalid_username(self):
        """
        Ensure POST request with invalid `username` does not
        logins a user.
        """
        self.user.set_password('password')
        self.user.save()
        payload = {
            'username': 'invalid_username',
            'password': 'password'
        }
        response = self.client.post(self.url, payload)
        self.assertTemplateUsed(response, self.template)
        self.assertContains(response, 'Please enter a correct credential.')

    def test_post_request_with_invalid_password(self):
        """
        Ensure POST request with invalid `invalid` does not
        logins a user.
        """
        self.user.set_password('password')
        self.user.save()
        payload = {
            'username': self.user.username,
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, payload)
        self.assertTemplateUsed(response, self.template)
        self.assertContains(response, 'Please enter a correct credential.')
