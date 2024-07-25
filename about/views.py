from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    about_ceo = About.objects.last()
    context = {
        'about_ceo':about_ceo,
    }
    return render(request , 'about_ceo.html' , context)