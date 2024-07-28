from django.shortcuts import render
from products.models import Product
from aboutus.models import AboutUS , FAQ
from services.models import Services
# Create your views here.
def home(request):
    about = AboutUS.objects.last()
    faqs = FAQ.objects.all()
    services = Services.objects.all()[:4]

    context = {
        'about':about,
        'faqs':faqs,
        'services':services,
    }
    return render(request , 'home.html' , context)

