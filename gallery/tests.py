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

    def test_save_category(self):
        self.category.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.category.save_category()
        self.category.delete_category()
        category=Category.objects.all()
        self.assertTrue(len(category)<=0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.location=Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        locations=Location.get_locations()
        self.assertTrue(len(locations)>0)

    def test_get_location(self):
        self.location.save_location()
        locations=Location.get_locations()
        self.assertTrue(len(locations)>=1)