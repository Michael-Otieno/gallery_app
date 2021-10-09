from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):
    #Set up
    def setUp(self):
        self.category=Category(name='Tour')
        # self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))