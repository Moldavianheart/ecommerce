from django.db import models
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60)
    summary = models.TextField()
    description = models.TextField()
    price = models.CharField(max_length=6)
    old_price = models.CharField(max_length=6)
    slug = models.SlugField()
    image_id = models.IntegerField()
    release_date = models.DateField()

class ProductImage(models.Model):
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.CharField(max_length=255)
	thumb = models.CharField(max_length=255)
	date  = models.DateTimeField()
