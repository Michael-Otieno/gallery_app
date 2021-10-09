from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description=models.TextField()
    author=models.CharField(max_length=60,default='admin')
    pub_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

