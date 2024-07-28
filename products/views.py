from django.shortcuts import render
from .models import Product
from django.db.models.query_utils import Q


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

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q :
            product = Product.objects.filter(
                Q(description__icontains=q ) |
                Q( name__icontains=q) |
                Q(category__name__icontains=q)
                )
        else :
            return render(request , 'products.html')
    context = {
        'products':product , 
    }
    return render(request , 'products.html', context)