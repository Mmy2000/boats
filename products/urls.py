from django.urls import path
from . import views

urlpatterns = [
    path('' , views.product_list , name="product_list"),
    path('parts/' , views.parts , name="parts"),
    path('on_sale/' , views.on_sale , name="on_sale")
]