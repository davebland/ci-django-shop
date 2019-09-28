from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """ Tests for product model """
    def test_str(self):
        test_name = Product(name='A test product')
        self.assertEqual(str(test_name), 'A test product')