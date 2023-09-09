from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Menu

class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Menu.objects.create(name='Pizza', price=10.99, description='Delicious pizza')

    def test_name_label(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_price_label(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_description_label(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_name_max_length(self):
        menu = Menu.objects.get(id=1)
        max_length = menu._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_price_not_null(self):
        menu = Menu.objects.get(id=1)
        not_null = menu._meta.get_field('price').null
        self.assertFalse(not_null)

    def test_description_default_value(self):
        menu = Menu.objects.get(id=1)
        default_value = menu._meta.get_field('description').default
        self.assertEqual(default_value, '')