from django.contrib import admin
from .models import Services , ServicesImages
from django_summernote.admin import SummernoteModelAdmin
import admin_thumbnails


# Register your models here.


@admin_thumbnails.thumbnail('image')
class ServiceGallaryInline(admin.TabularInline):
    model = ServicesImages
    extra = 1

class ModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [ServiceGallaryInline]

admin.site.register(Services,ModelAdmin)
admin.site.register(ServicesImages)