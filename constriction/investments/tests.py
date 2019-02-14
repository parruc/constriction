from django.test import Client
from django.test import TestCase

# Create your tests here.

class TestMainNavigation(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        homepage = self.client.get('/')
        self.assertTrue(homepage.status_code, 200)
        self.assertTemplateUsed(homepage, 'home.html')
