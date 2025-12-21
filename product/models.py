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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )
    size = models.IntegerField()
    country = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/',default='product/default.jpg',blank=True,null=True)

    def avr_rate(self):
        rates = [i.rate for i in self.comments.all() if i.rate > 0]
        return round(sum(rates) / len(rates), 1) if len(rates) > 0 else 0

    def __str__(self):
        return f'{self.name},{self.category}'


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_comments')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    rate = models.PositiveIntegerField(default=0, blank=True,null=True)
    image_comment = models.ImageField(upload_to='comment/',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.text



