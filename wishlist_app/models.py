from django.db import models

class Client(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=150)
  email = models.EmailField(blank=False, max_length=150, unique=True)

  def __str__(self):
    return self.name

class Product(models.Model):
  id = models.AutoField(primary_key=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='product_img')
  brand = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  reviewScore = models.FloatField(max_length=4, decimal_places=2)

  def __str__(self):
    return self.title

class Fav_Product(models.Model):
  client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)
  product = models.ManyToManyField(Product, related_name='wishlist')

  class Meta:
    unique_together = [['client']]