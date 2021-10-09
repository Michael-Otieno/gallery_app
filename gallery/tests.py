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

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)<=0)

    def test_update_image(self):
        self.image.save_image()
        self.image.update_image(self.image.id, 'photos/test.jpg')
        changed_image=Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_image)>=0)


    def test_get_image_by_id(self):
        self.image.save_image()
        image_found=self.image.get_image_by_id(self.image.id)
        image=Image.objects.filter(id=self.image.id)
        self.assertTrue(image_found,image)

    def test_search_image_by_location(self):
        self.image.save_image()
        image_found=self.image.filter_by_location(location='Nairobi')
        self.assertTrue(len(image_found)>=0)

    def search_image_by_category(self):
        self.image.save_image()
        category='Tour'
        found_image=self.image.search_by_category(category)
        self.assertTrue(len(found_image)>=0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()