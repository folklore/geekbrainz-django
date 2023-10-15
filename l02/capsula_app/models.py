from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(null=False,
                            blank=False,
                            max_length=120)
    email = models.EmailField(null=False,
                              blank=False,
                              unique=True)
    phone = PhoneNumberField(null=False,
                             blank=False,
                             unique=True)
    address = models.CharField(null=False,
                               blank=False,
                               max_length=360)
    created_on = models.DateField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(null=False,
                             blank=False,
                             max_length=240)
    description = models.TextField(null=False,
                                   blank=False,
                                   max_length=4800)
    cost = models.DecimalField(null=False,
                               max_digits=8,
                               decimal_places=2)
    count = models.IntegerField(null=False)

    created_on = models.DateField(auto_now_add=True)


class Order(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2)
    created_on = models.DateField(auto_now_add=True)
