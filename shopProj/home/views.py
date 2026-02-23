from django.shortcuts import render, redirect
from product.models import Product

def home(request):
    products = Product.objects.all().order_by('-created')
    #products = Product.objects_2.all()
    #products = Product.objects_2.buyable()
    return render(request, 'home/index.html', {'products': products})


