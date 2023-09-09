from django.test import TestCase
from restaurant.models import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class MenuTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = User.objects.create_user(username='abc', password='123')
    self.client.login(username='abc', password='123')

    Menu.objects.create(name="Pizza", description="Margherita", price=10.00)
    Menu.objects.create(name="Pasta", description="Spaghetti", price=12.00)
    Menu.objects.create(name="Salad", description="Caesar", price=8.00)

  def test_menu_list(self):
    response = self.client.get('/api/menu/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 3)

  def test_menu_detail(self):
    response = self.client.get('/api/menu/1/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['name'], 'Pizza')