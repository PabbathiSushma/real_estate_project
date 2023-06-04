from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    nums_bedrooms = models.IntegerField()
    nums_bathrooms = models.IntegerField()
    sqaure_footage = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title