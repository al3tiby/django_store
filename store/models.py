from django.contrib.sessions.models import Session
from django.db import models

from checkout.models import Transaction
from django_store import settings

# Create your models here.
from django.db.models import PROTECT


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField()
    pdf_file = models.FileField(null=True)
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    @property
    def pdf_file_url(self):
        return settings.SITE_URL + self.pdf_file.url

    def __str__(self):
        return self.name




class Order(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)



class OrdersProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=PROTECT)
    product = models.ForeignKey(Product, on_delete=PROTECT)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)



class Cart(models.Model):
    items = models.JSONField(default=dict)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)



class Slider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(max_length=255)
    image = models.ImageField(null=True)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title