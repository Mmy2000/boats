from django.shortcuts import render
from products.models import Product
from aboutus.models import AboutUS , FAQ
from services.models import Services
from .models import Images , NewsLitter
from django.http import JsonResponse


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

def newsletters(request):
    email = request.POST.get('email')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'message': 'Subscribed successfully'})