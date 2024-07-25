from django.shortcuts import render
from .models import AboutUS , FAQ
# Create your views here.

def about(request):
    about = AboutUS.objects.last()
    faqs = FAQ.objects.all()
    context = {
        'about':about,
        'faqs':faqs
    }
    return render(request , 'about_us.html' , context)