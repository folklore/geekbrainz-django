from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Product, Order
from datetime import datetime, timedelta
from .forms import ProductForm



def listing(request, interval):
    if interval == 'month':
        days = 30
    elif interval == 'year':
        days = 365
    else:
        days = 7

    orders = Order.objects.filter(created_on__gte=datetime.today() - timedelta(days=days)).order_by('-created_on')
    return render(request, 'capsula/listing.html', {'orders': orders})


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)

    return render(request, 'capsula/products/form.html', {'form': form, 'product': product})


def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=product)

    if form.is_valid():
        form.save()
        return redirect('listing', 'month')

    return render(request, 'capsula/products/form.html', {'form': form, 'product': product})
