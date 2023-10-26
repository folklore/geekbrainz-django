from django.db import models
from django.contrib import admin
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

admin.site.register(Client)


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

    cover = models.ImageField(upload_to = 'images/')

    created_on = models.DateField(auto_now_add=True)


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost', 'count']
    list_filter = ['created_on', 'cost']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию товара'
    actions = [reset_quantity]
    readonly_fields = ['created_on']


admin.site.register(Product, ProductAdmin)


class Order(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2)
    created_on = models.DateField(auto_now_add=True)

admin.site.register(Order)
