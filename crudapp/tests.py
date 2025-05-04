from django.test import TestCase
from .models import Farmer, Product

class FarmerModelTest(TestCase):
    def setUp(self):
        self.farmer = Farmer.objects.create(
            name='Test Farmer',
            email='testfarmer@example.com',
            phone_number='1234567890',
            location='Test Location',
            password='testpassword'
        )

    def test_farmer_creation(self):
        self.assertEqual(self.farmer.name, 'Test Farmer')
        self.assertEqual(self.farmer.email, 'testfarmer@example.com')
        self.assertEqual(self.farmer.phone_number, '1234567890')
        self.assertEqual(self.farmer.location, 'Test Location')

class ProductModelTest(TestCase):
    def setUp(self):
        self.farmer = Farmer.objects.create(
            name='Test Farmer',
            email='testfarmer@example.com',
            phone_number='1234567890',
            location='Test Location',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            stock=100,
            deposit_percentage=5.00,
            farmer=self.farmer
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 10.00)
        self.assertEqual(self.product.stock, 100)
        self.assertEqual(self.product.deposit_percentage, 5.00)
        self.assertEqual(self.product.farmer, self.farmer)