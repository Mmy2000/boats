from django.shortcuts import render
from .models import Product
# Create your views here.
def product_list(request):
    products = Product.objects.prefetch_related('productgallary_set').all()
    context = {
        'products':products
    }
    return render(request , 'products.html' , context)

def parts(request):
    products = Product.objects.filter(category__name= 'Parts')
    context = {
        'products':products
    }
    return render(request , 'products.html' , context)

def on_sale(request):
    products = Product.objects.filter(category__name= 'Boats for sales')
    context = {
        'products':products
    }
    return render(request , 'products.html' , context)