from django.shortcuts import render

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            subject = "Welcome to Z Marketing site"
            message = "Our team will contact you within 24hrs."
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email']
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list])
            messages.success(request, 'Your Message send successfully.')
        else:
            messages.error(request, 'Pls try agian.')
    else:
        form = ContactForm()
    # context = {'form':form}

    return render(request , 'contact.html' )