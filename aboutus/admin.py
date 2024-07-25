from django.contrib import admin
from .models import AboutUS , FAQ
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(AboutUS,ModelAdmin)
admin.site.register(FAQ)