from django.shortcuts import render
from products.models import Product
# Create your views here.
def home(request):
    return render(request , 'home.html')

