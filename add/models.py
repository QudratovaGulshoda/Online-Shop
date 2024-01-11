from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here

class Category(BaseModel):
    name=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name


class Ad(BaseModel):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ads_image/')
    content = models.TextField()
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    category = models.ManyToManyField(Category, related_name='categories')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def picture(self):
        return format_html('<img src="{}" width="50" heigth="50" style="border-radius:50%"/>'.format(self.image.url))

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def all_products(self):
        basket = self.baskets.all()
        return sum([i.quantity for i in basket])

    @property
    def all_price(self):
        basket = self.baskets.all()
        return sum([i.xaridnarx for i in basket])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='baskets')
    product = models.ForeignKey(Ad, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order} ning xaridi!"

    @property
    def narx(self):
        return self.product.price

    @property
    def xaridnarx(self):
        return self.product.price * self.quantity
