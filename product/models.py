from django.conf import settings
from django.db import models



# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    ower = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='product',blank=True,null=True)
    size = models.IntegerField()
    country = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/',default='product/default.jpg',blank=True,null=True)

    def __str__(self):
        return f'{self.name},{self.category}'


class Comments(models.Model):


