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

    def test_update_location(self):
        self.location.save_location()
        location=Location.objects.filter(name='Nairobi').update(name='Kisumu')
        self.updated_location=Location.objects.get(name='Kisumu')
        self.assertEqual(self.updated_location.name,'Kisumu')

    def test_delete_location(self):
        self.location.save_location()
        self.location.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location)==0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.location=Location(name='Nairobi')
        self.location.save_location()

        self.category=Category(name='Tour')
        self.category.save_category()

        self.image=Image(id=1,name='image',description='description test', location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
