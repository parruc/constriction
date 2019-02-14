from django.test import Client
from django.test import TestCase
from django.utils import timezone
from investments.models import BaseInvestment

# Create your tests here.

class TestBaseInvestment(TestCase):

    def create_base_investment(self, title="only a test", description="yes, this is only a test", price=10):
        return BaseInvestment.objects.create(title=title, description=description, price=price)

    def test_base_investment_creation(self):
        w = self.create_base_investment()
        self.assertTrue(isinstance(w, BaseInvestment))
        self.assertEqual(w.__str__(), w.title)


class TestMainNavigation(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        homepage = self.client.get('/')
        self.assertTrue(homepage.status_code, 200)
        self.assertTemplateUsed(homepage, 'home.html')
