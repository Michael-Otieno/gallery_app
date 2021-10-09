from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    name=models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations=Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description=models.TextField()
    author=models.CharField(max_length=60,default='admin')
    pub_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def filter_by_location(cls,location):
        image_location=Image.objects.filter(name=location).all()
        return image_location

    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.filter(id=id).all()
        return image



    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    