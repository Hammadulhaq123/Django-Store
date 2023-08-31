from django.db import models

# Create your models here.


class Ecommerce(models.Model):
    title = models.CharField(max_length=30)
    tag = models.CharField(max_length=7)
    rating = models.IntegerField(default=1)
    price = models.IntegerField(default=500)
    image = models.ImageField(upload_to="store_images")
