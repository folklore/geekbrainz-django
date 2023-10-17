from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order
from datetime import datetime, timedelta


def listing(request, interval):
    if interval == 'month':
        days = 30
    elif interval == 'year':
        days = 365
    else:
        days = 7

    orders = Order.objects.filter(created_on__gte=datetime.today() - timedelta(days=days)).order_by('-created_on')

    return render(request, 'capsula/listing.html', {'orders': orders})
