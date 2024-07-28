from django.shortcuts import render
from products.models import Product
from aboutus.models import AboutUS , FAQ
from services.models import Services
from .models import Images
# Create your views here.
def home(request):
    about = AboutUS.objects.last()
    faqs = FAQ.objects.all()
    services = Services.objects.all()[:4]
    images = Images.objects.all()

    context = {
        'about':about,
        'faqs':faqs,
        'services':services,
        'images':images,
    }
    return render(request , 'home.html' , context)

