from . import views
from django.urls import path


urlpatterns = [
    path('' , views.services , name='services'),
    path('<slug:category_slug>/', views.services, name='services_by_category'),
    path('<str:slug>' , views.service_details , name='service_details'),
]