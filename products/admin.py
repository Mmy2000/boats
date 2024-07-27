from django.contrib import admin
from .models import Product , ProductGallary , Category
from django_summernote.admin import SummernoteModelAdmin


import admin_thumbnails
# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGallaryInline(admin.TabularInline):
    model = ProductGallary
    extra = 1

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name' , 'price' ,  'category' , 'created_at' , 'is_available')
    summernote_fields = '__all__'
    inlines = [ProductGallaryInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductGallary)
admin.site.register(Category)