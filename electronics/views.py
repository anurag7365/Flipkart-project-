from django.shortcuts import render
from .models import Product

# Create your views here.

#home page link
def home(request):
    return render(request,'electronics/home.html')


#details page link of the products
def product_details(request):
    prod = Product.objects.all()
    return render(request,'electronics/product_details.html',{"prod":prod})

