from django.shortcuts import render
from django.http import HttpResponse
from .models import Product 


def index(request):
    products = Product.objects.all()
<<<<<<< HEAD
    return  render(request,'index.html', {'products':products})






=======
    return  render(request,'index.html', {'products':products})
>>>>>>> c1de626480fc5a2c29cce6e82bc9c6ef347af0ee
