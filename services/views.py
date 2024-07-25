from django.shortcuts import render , get_object_or_404
from .models import Services , CategoryService
# Create your views here.



def services(request, category_slug=None):
    categories = CategoryService.objects.all()
    services = None
    selected_category = None
    
    if category_slug:
        selected_category = get_object_or_404(CategoryService, slug=category_slug)
        services = Services.objects.filter(category=selected_category)
    else:
        services = Services.objects.all()
    
    context = {
        'categories': categories,
        'services': services,
        'selected_category': selected_category,
    }
    return render(request, 'services.html', context)




def service_details(request,slug):
    service_detail = Services.objects.get(slug=slug)
    context = {
        'service_detail':service_detail
    }
    return render(request , 'service_detail.html' , context)