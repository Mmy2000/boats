from django.shortcuts import render
from .models import AboutUS
# Create your views here.

def about(request):
    about = AboutUS.objects.last()
    context = {
        'about':about
    }
    return render(request , 'about_us.html' , context)